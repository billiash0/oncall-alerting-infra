# oncall-alerting-infra
Grafana OnCall + n8n alerting infrastructure
# для корректного запуска после команды 
тобы все работало с чистой коробки нужно сделать следующее 
запустить докер docker coompose up -d 
потом зайти на http://localhost:3000/a/grafana-oncall-app и там нажать на коннект (выдаст ошибку)
дальше в терминале ввести 
cd ~/workN1/oncall-alerting-infra
docker compose exec -T oncall-engine python manage.py shell < gan.py
в котором находится 
from apps.user_management.models import Organization
org = Organization.objects.first()
print('Current grafana_url:', org.grafana_url)
org.grafana_url = 'http://oncall-grafana:3000'
org.save(update_fields=['grafana_url'])
print('Fixed!')
и заново нажать коннект