# coding: utf-8

from django import forms


class DingDingOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token-test'
    )
    ignore_regular = forms.CharField(
        max_length=255,
        help_text='忽略错误信息的正则表达式'
    )
    highest_level_regular = forms.CharField(
        max_length=255,
        help_text='高危等级错误正则表达式'
    )
    medium_level_regular = forms.CharField(
        max_length=255,
        help_text='中危等级错误正则表达式'
    )
    low_level_regular = forms.CharField(
        max_length=255,
        help_text='低危等级错误正则表达式'
    )