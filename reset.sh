#!/bin/bash
echo "==> Проверяем организации в OnCall..."

docker compose exec -T oncall-engine python manage.py shell << 'EOF'
from apps.user_management.models import Organization
count = Organization.objects.count()
print('Orgs in DB:', count)
for o in Organization.objects.all():
    print('  stack_id=%s  grafana_url=%s' % (o.stack_id, o.grafana_url))
EOF

echo ""
echo "==> Готово. Открой http://localhost:3000"
echo "    Grafana -> Administration -> Plugins -> OnCall -> Connect"