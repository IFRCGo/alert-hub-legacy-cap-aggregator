from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.db import models
from django.utils import timezone

import cap_feed.data_injector as di
import cap_feed.formats.format_handler as fh
from .models import Alert, AlertInfo, Feed, ProcessedAlert



@shared_task(bind=True)
def poll_feed(self, url):
    polled_alerts_count = 0
    try:
        feed = Feed.objects.get(url=url)
        if not feed.enable_polling:
            return f"Feed with url {url} is disabled for polling"
        polled_alerts_count += fh.get_alerts(feed)
    except Feed.DoesNotExist:
        print(f"Feed with url {url} does not exist")
    return f"polled {polled_alerts_count} alerts from {feed.url}"

@shared_task(bind=True)
def remove_expired_alerts(self):
    # Remove valid alerts that have expired
    AlertInfo.objects.filter(expires__lt=timezone.now()).delete()
    expired_alerts = Alert.objects.filter(infos__isnull=True)
    expired_alerts_count = expired_alerts.count()
    expired_alerts.delete()
    return f"removed {expired_alerts_count} alerts"


@shared_task(bind=True)
def remove_expired_alerts(self):
    # Tag valid alerts that have expired
    expired_alerts = (
        Alert.objects.filter(is_expired=False)
        .annotate(
            active_alert_info_count=models.Count(
                'infos',
                filter=models.Q(
                    infos__expires__gt=timezone.now(),
                ),
            ),
        )
        .filter(active_alert_info_count=0)
    )

    expired_alerts_count = expired_alerts.count()
    expired_alerts.update(is_expired=True)

    return f"tag {expired_alerts_count} alerts as expired"


@shared_task(bind=True)
def inject_data(self):
    di.inject_geographical_data()
    di.inject_feeds()
    return f"injected data"
