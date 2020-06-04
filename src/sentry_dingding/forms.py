# coding: utf-8

from django import forms


class DingDingOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token-test'
    )
    ignore_regular = forms.CharField(
        max_length=255,
        help_text='Ignore regular expressions for this information'
    )
    highest_level_regular = forms.CharField(
        max_length=255,
        help_text='Regular expression of highest risk error information',
        required = False
    )
    medium_level_regular = forms.CharField(
        max_length=255,
        help_text='Regular expression of medium risk error information'
    )
    low_level_regular = forms.CharField(
        max_length=255,
        help_text='Regular expression of low risk error information'
    )