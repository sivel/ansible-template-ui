FROM alpine
MAINTAINER Matt Martz <matt@sivel.net>

COPY clean_collections.py /tmp/clean_collections.py
COPY execute.sh /execute.sh
COPY playbook.yml /playbook.yml

RUN set -x && \
    apk add -U python3 py3-pip openssl-dev python3-dev libffi-dev ca-certificates gcc make musl-dev git yaml-dev && \
    pip3 install -U pip && \
    pip3 install https://github.com/ansible/ansible/archive/devel.tar.gz jmespath netaddr && \
    apk del openssl-dev python2-dev libffi-dev gcc make musl musl-dev git yaml pkgconf

RUN set -x && \
    ansible-galaxy collection install --pre \
        amazon.aws \
        ansible.netcommon \
        ansible.posix \
        ansible.windows \
        arista.eos \
        awx.awx \
        azure.azcollection \
        check_point.mgmt \
        chocolatey.chocolatey \
        cisco.aci \
        cisco.asa \
        cisco.intersight \
        cisco.ios \
        cisco.iosxr \
        cisco.meraki \
        cisco.mso \
        cisco.nso \
        cisco.nxos \
        cisco.ucs \
        cloudscale_ch.cloud \
        community.aws \
        community.azure \
        community.crypto \
        community.digitalocean \
        community.docker \
        community.general \
        community.grafana \
        community.hrobot \
        community.kubernetes \
        community.libvirt \
        community.mongodb \
        community.mysql \
        community.network \
        community.okd \
        community.postgresql \
        community.proxysql \
        community.rabbitmq \
        community.routeros \
        community.skydive \
        community.vmware \
        community.windows \
        community.zabbix \
        containers.podman \
        cyberark.conjur \
        cyberark.pas \
        dellemc.os10 \
        dellemc.os6 \
        dellemc.os9 \
        f5networks.f5_modules \
        fortinet.fortimanager \
        fortinet.fortios \
        frr.frr \
        gluster.gluster \
        google.cloud \
        hetzner.hcloud \
        ibm.qradar \
        infinidat.infinibox \
        junipernetworks.junos \
        mellanox.onyx \
        netapp.aws \
        netapp.elementsw \
        netapp_eseries.santricity \
        netapp.ontap \
        netbox.netbox \
        ngine_io.cloudstack \
        ngine_io.exoscale \
        ngine_io.vultr \
        openstack.cloud \
        openvswitch.openvswitch \
        ovirt.ovirt \
        purestorage.flasharray \
        purestorage.flashblade \
        servicenow.servicenow \
        splunk.es \
        theforeman.foreman \
        vyos.vyos \
        wti.remote && \
    python3 /tmp/clean_collections.py

CMD ["/bin/sh", "/execute.sh"]
