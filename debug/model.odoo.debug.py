#!/usr/bin/python3

# set server timezone in UTC before time module imported
__import__('os').environ['TZ'] = 'UTC'
import odoo
import debugpy

debugpy.listen(("0.0.0.0", 5678))
if __name__ == "__main__":
    odoo.cli.main()
