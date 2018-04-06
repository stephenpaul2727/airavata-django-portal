# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-21 16:29
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.blocks.static_block
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('django_airavata_wagtail_base', '0056_auto_20180321_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph_block', wagtail.core.blocks.StructBlock((('custom_class', wagtail.core.blocks.TextBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('width', wagtail.core.blocks.IntegerBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.core.blocks.StructBlock((('embed', wagtail.embeds.blocks.EmbedBlock()), ('custom_class', wagtail.core.blocks.TextBlock())))), ('bootstrap_jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.TextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False)), ('is_link', wagtail.core.blocks.BooleanBlock(required=False)), ('alert_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_card', wagtail.core.blocks.StructBlock((('card_width', wagtail.core.blocks.IntegerBlock(help_text='18 works best for card')), ('is_card_img', wagtail.core.blocks.BooleanBlock(required=False)), ('card_img', wagtail.images.blocks.ImageChooserBlock(required=False)), ('card_title', wagtail.core.blocks.TextBlock()), ('card_text', wagtail.core.blocks.RichTextBlock()), ('card_bg_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('bg-primary', 'DEFAULT'), ('bg-secondary', 'GREY'), ('bg-success', 'GREEN'), ('bg-danger', 'RED'), ('bg-warning', 'ORANGE'), ('bg-dark', 'DARK'), ('bg-light', 'LIGHT')], required=False)), ('btn_text', wagtail.core.blocks.TextBlock(required=False)), ('btn_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('btn_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_carousel', wagtail.core.blocks.StructBlock((('c_image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('c_image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('row_separator', wagtail.core.blocks.static_block.StaticBlock(icon='fa-cut', template='blocks/bootstrap/ann.html'))), blank=True, null=True, verbose_name='About content block'),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph_block', wagtail.core.blocks.StructBlock((('custom_class', wagtail.core.blocks.TextBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('width', wagtail.core.blocks.IntegerBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.core.blocks.StructBlock((('embed', wagtail.embeds.blocks.EmbedBlock()), ('custom_class', wagtail.core.blocks.TextBlock())))), ('bootstrap_jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.TextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False)), ('is_link', wagtail.core.blocks.BooleanBlock(required=False)), ('alert_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_card', wagtail.core.blocks.StructBlock((('card_width', wagtail.core.blocks.IntegerBlock(help_text='18 works best for card')), ('is_card_img', wagtail.core.blocks.BooleanBlock(required=False)), ('card_img', wagtail.images.blocks.ImageChooserBlock(required=False)), ('card_title', wagtail.core.blocks.TextBlock()), ('card_text', wagtail.core.blocks.RichTextBlock()), ('card_bg_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('bg-primary', 'DEFAULT'), ('bg-secondary', 'GREY'), ('bg-success', 'GREEN'), ('bg-danger', 'RED'), ('bg-warning', 'ORANGE'), ('bg-dark', 'DARK'), ('bg-light', 'LIGHT')], required=False)), ('btn_text', wagtail.core.blocks.TextBlock(required=False)), ('btn_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('btn_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_carousel', wagtail.core.blocks.StructBlock((('c_image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('c_image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('row_separator', wagtail.core.blocks.static_block.StaticBlock(icon='fa-cut', template='blocks/bootstrap/ann.html'))), blank=True, null=True, verbose_name='Contact content block'),
        ),
        migrations.AlterField(
            model_name='documentationpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph_block', wagtail.core.blocks.StructBlock((('custom_class', wagtail.core.blocks.TextBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('width', wagtail.core.blocks.IntegerBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.core.blocks.StructBlock((('embed', wagtail.embeds.blocks.EmbedBlock()), ('custom_class', wagtail.core.blocks.TextBlock())))), ('bootstrap_jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.TextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False)), ('is_link', wagtail.core.blocks.BooleanBlock(required=False)), ('alert_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_card', wagtail.core.blocks.StructBlock((('card_width', wagtail.core.blocks.IntegerBlock(help_text='18 works best for card')), ('is_card_img', wagtail.core.blocks.BooleanBlock(required=False)), ('card_img', wagtail.images.blocks.ImageChooserBlock(required=False)), ('card_title', wagtail.core.blocks.TextBlock()), ('card_text', wagtail.core.blocks.RichTextBlock()), ('card_bg_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('bg-primary', 'DEFAULT'), ('bg-secondary', 'GREY'), ('bg-success', 'GREEN'), ('bg-danger', 'RED'), ('bg-warning', 'ORANGE'), ('bg-dark', 'DARK'), ('bg-light', 'LIGHT')], required=False)), ('btn_text', wagtail.core.blocks.TextBlock(required=False)), ('btn_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('btn_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_carousel', wagtail.core.blocks.StructBlock((('c_image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('c_image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('row_separator', wagtail.core.blocks.static_block.StaticBlock(icon='fa-cut', template='blocks/bootstrap/ann.html'))), blank=True, null=True, verbose_name='Documentation content block'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph_block', wagtail.core.blocks.StructBlock((('custom_class', wagtail.core.blocks.TextBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('width', wagtail.core.blocks.IntegerBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.core.blocks.StructBlock((('embed', wagtail.embeds.blocks.EmbedBlock()), ('custom_class', wagtail.core.blocks.TextBlock())))), ('bootstrap_jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.TextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False)), ('is_link', wagtail.core.blocks.BooleanBlock(required=False)), ('alert_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_card', wagtail.core.blocks.StructBlock((('card_width', wagtail.core.blocks.IntegerBlock(help_text='18 works best for card')), ('is_card_img', wagtail.core.blocks.BooleanBlock(required=False)), ('card_img', wagtail.images.blocks.ImageChooserBlock(required=False)), ('card_title', wagtail.core.blocks.TextBlock()), ('card_text', wagtail.core.blocks.RichTextBlock()), ('card_bg_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('bg-primary', 'DEFAULT'), ('bg-secondary', 'GREY'), ('bg-success', 'GREEN'), ('bg-danger', 'RED'), ('bg-warning', 'ORANGE'), ('bg-dark', 'DARK'), ('bg-light', 'LIGHT')], required=False)), ('btn_text', wagtail.core.blocks.TextBlock(required=False)), ('btn_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('btn_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_carousel', wagtail.core.blocks.StructBlock((('c_image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('c_image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('row_separator', wagtail.core.blocks.static_block.StaticBlock(icon='fa-cut', template='blocks/bootstrap/ann.html'))), blank=True, null=True, verbose_name='Home content block'),
        ),
        migrations.AlterField(
            model_name='rowblankpagerelation',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph_block', wagtail.core.blocks.StructBlock((('custom_class', wagtail.core.blocks.TextBlock(required=False)), ('body', wagtail.core.blocks.RichTextBlock())))), ('image_block', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False)), ('width', wagtail.core.blocks.IntegerBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('embed_block', wagtail.core.blocks.StructBlock((('embed', wagtail.embeds.blocks.EmbedBlock()), ('custom_class', wagtail.core.blocks.TextBlock())))), ('bootstrap_jumbotron', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock()), ('body', wagtail.core.blocks.RichTextBlock()), ('button_text', wagtail.core.blocks.TextBlock(required=False)), ('button_link', wagtail.core.blocks.TextBlock(required=False)), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_alert', wagtail.core.blocks.StructBlock((('alert_text', wagtail.core.blocks.TextBlock()), ('alert_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('alert-primary', 'DEFAULT'), ('alert-secondary', 'GREY'), ('alert-success', 'GREEN'), ('alert-danger', 'RED'), ('alert-warning', 'ORANGE'), ('alert-dark', 'DARK'), ('alert-light', 'LIGHT')], required=False)), ('is_link', wagtail.core.blocks.BooleanBlock(required=False)), ('alert_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_button', wagtail.core.blocks.StructBlock((('button_text', wagtail.core.blocks.TextBlock()), ('button_link', wagtail.core.blocks.TextBlock()), ('button_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('button_size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'DEFAULT'), ('btn-lg', 'LARGE'), ('btn-sm', 'SMALL')], required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_card', wagtail.core.blocks.StructBlock((('card_width', wagtail.core.blocks.IntegerBlock(help_text='18 works best for card')), ('is_card_img', wagtail.core.blocks.BooleanBlock(required=False)), ('card_img', wagtail.images.blocks.ImageChooserBlock(required=False)), ('card_title', wagtail.core.blocks.TextBlock()), ('card_text', wagtail.core.blocks.RichTextBlock()), ('card_bg_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('bg-primary', 'DEFAULT'), ('bg-secondary', 'GREY'), ('bg-success', 'GREEN'), ('bg-danger', 'RED'), ('bg-warning', 'ORANGE'), ('bg-dark', 'DARK'), ('bg-light', 'LIGHT')], required=False)), ('btn_text', wagtail.core.blocks.TextBlock(required=False)), ('btn_color', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('btn-primary', 'DEFAULT'), ('btn-danger', 'RED'), ('btn-secondary', 'GREY'), ('btn-success', 'GREEN'), ('btn-warning', 'ORANGE')], required=False)), ('btn_link', wagtail.core.blocks.TextBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('bootstrap_carousel', wagtail.core.blocks.StructBlock((('c_image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('c_image2', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image3', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image4', wagtail.images.blocks.ImageChooserBlock(required=False)), ('c_image5', wagtail.images.blocks.ImageChooserBlock(required=False)), ('custom_class', wagtail.core.blocks.TextBlock(required=False))))), ('row_separator', wagtail.core.blocks.static_block.StaticBlock(icon='fa-cut', template='blocks/bootstrap/ann.html'))), blank=True, null=True, verbose_name='Row Content'),
        ),
    ]