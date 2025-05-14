docker exec -it sge-odoo-web-1 bash

odoo \
  --config=/etc/odoo/odoo.conf \
  -d odoo \
  -i base \
  --without-demo=all \
  --stop-after-init
