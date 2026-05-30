from apps.user_management.models import Organization
org = Organization.objects.first()
print('Current grafana_url:', org.grafana_url)
org.grafana_url = 'http://oncall-grafana:3000'
org.save(update_fields=['grafana_url'])
print('Fixed!')