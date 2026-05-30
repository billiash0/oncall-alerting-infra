from apps.user_management.models import Organization
org = Organization.objects.first()
print('Current grafana_url:', org.grafana_url)
org.grafana_url = 'http://oncall-grafana:3000'
org.save(update_fields=['grafana_url'])
print('Fixed!')
# Разовый фикс: OnCall при install сохранил grafana_url = http://localhost:3000
# (это URL из браузера), но изнутри контейнера localhost — это сам движок, не Grafana.
# Меняем на внутренний Docker-адрес чтобы синк пользователей/команд работал корректно.