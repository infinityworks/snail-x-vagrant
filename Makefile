up: 
	vagrant up

prov: 
	vagrant provision

restart:
	vagrant destroy
	vagrant up

core:
	vagrant ssh -c "/vagrant/core.sh"

front:
	vagrant ssh -c "/vagrant/front.sh"

feed:
	vagrant ssh -c "/vagrant/feed.sh" 
