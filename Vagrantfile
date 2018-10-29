# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.network "forwarded_port", guest: 8080, host: 8081
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end

  config.vm.synced_folder "../snail-x-core", "/vagrant/snail-x-core"
  config.vm.synced_folder "../snail-x-feed-handler", "/vagrant/snail-x-feed-handler"
  config.vm.synced_folder "../snail-x-vue", "/vagrant/snail-x-vue"
end
