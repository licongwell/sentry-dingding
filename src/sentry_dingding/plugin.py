# coding: utf-8

import json
import logging

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_dingding
from .forms import DingDingOptionsForm

DingTalk_API = "https://oapi.dingtalk.com/robot/send?access_token={token}"


class DingDingPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to DingDing.
    """
    author = 'ansheng'
    author_url = 'https://github.com/anshengme/sentry-dingding'
    version = sentry_dingding.VERSION
    description = 'Send error counts to DingDing.'
    resource_links = [
        ('Source', 'https://github.com/anshengme/sentry-dingding'),
        ('Bug Tracker', 'https://github.com/anshengme/sentry-dingding/issues'),
        ('README', 'https://github.com/anshengme/sentry-dingding/blob/master/README.md'),
    ]

    slug = 'DingDing'
    title = 'DingDing'
    conf_key = slug
    conf_title = title
    project_conf_form = DingDingOptionsForm

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        access_token = self.get_option('access_token', group.project)

        # ignore_regular = self.get_option('ignore_regular', group.project)
        # highest_level_regular = self.get_option('highest_level_regular', group.project)
        # medium_level_regular = self.get_option('medium_level_regular', group.project)
        # low_level_regular = self.get_option('low_level_regular', group.project)
        

        send_url = DingTalk_API.format(token=access_token)

        self.getDingTitles(group, event, *args, **kwargs)

        title = u"**【高危】错误信息预警**来自 {}".format(event.project.slug)

        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "请注意！！",
                "text": u"#### {title} @18126450689 \n > {message} [href]({url})".format(
                    title=title,
                    message=event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event.id),
                ),
                "at": {
                    "atMobiles": [
                        "18126450689"
                    ]
                }
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
    def getDingTitles(self, group, event, *args, **kwargs):
        ignore_regular = self.get_option('ignore_regular', group.project)
        highest_level_regular = self.get_option('highest_level_regular', group.project)
        medium_level_regular = self.get_option('medium_level_regular', group.project)
        low_level_regular = self.get_option('low_level_regular', group.project)
        logging.warn('------分割sss-----')
        logging.warn(ignore_regular)
        logging.warn(highest_level_regular)
        logging.warn(medium_level_regular)   
        logging.warn(low_level_regular)
        logging.warn('------分割ssss-----')






