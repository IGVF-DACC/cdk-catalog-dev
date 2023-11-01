import aws_cdk as cdk

from constructs import Construct

from aws_cdk.aws_chatbot import SlackChannelConfiguration

from aws_cdk.aws_sns import Topic

from cdk_catalog_dev.constructs.slack import SlackWebhook

from typing import Any


class NotificationStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.encode_dcc_chatbot: SlackChannelConfiguration = SlackChannelConfiguration(
            self,
            'encode-dcc-aws-igvf-catalog-dev',
            slack_channel_configuration_name='aws-igvf-catalog-dev',
            slack_workspace_id='T1KMV4JJZ',
            slack_channel_id='C064J2FAK0Q',
        )
        self.alarm_notification_topic = Topic(
            self,
            'AlarmNotificationTopic',
        )
        self.encode_dcc_chatbot.add_notification_topic(
            self.alarm_notification_topic
        )
        self.encode_dcc_slack_webhook: SlackWebhook = SlackWebhook(
            self,
            'AwsIgvfCatalogDevSlackWebhook',
        )
