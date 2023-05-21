#
# Regular cron jobs for the penetration-app package.
#
0 4	* * *	root	[ -x /usr/bin/penetration-app_maintenance ] && /usr/bin/penetration-app_maintenance
