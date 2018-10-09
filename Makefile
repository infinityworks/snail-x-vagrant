up: 
	vagrant up

prov: 
	vagrant provision

restart:
	vagrant destroy
	vagrant up

core:
	vagrant ssh -c "/vagrant/core.sh"

feed:
	vagrant ssh -c "/vagrant/feed.sh" 
