# coding: utf-8

from django import forms


class DingDingOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token-test'
    )
    ignore_regular = forms.CharField(
        max_length=255,
        help_text='忽略错误信息正则表达式'
    )
    highest_levelRegular = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token-test'
    )
    medium_levelRegular = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token-test'
    )
    low_levelRegular = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token-test'
    )