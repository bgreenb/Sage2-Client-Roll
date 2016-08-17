Summary: Sage2 roll
Name: roll-Sage2
Version: 6.2
Release: 0
License: University of California
Vendor: Rocks Clusters
Group: System Environment/Base
Source: roll-Sage2-6.2.tar.gz
Buildroot: /work/Sage2_Client/roll-Sage2.buildroot
Prefix: /export/profile
Buildarch: noarch


%description
XML files for the Sage2 roll

%package kickstart
Summary: Sage2 roll
Group: System Environment/Base
%description kickstart
XML files for the Sage2 roll
%prep
%setup
%build
printf "\n\n\n### build ###\n\n\n"
BUILDROOT=/work/Sage2_Client/roll-Sage2.buildroot make -f /work/Sage2_Client/roll-Sage2.spec.mk build
%install
printf "\n\n\n### install ###\n\n\n"
BUILDROOT=/work/Sage2_Client/roll-Sage2.buildroot make -f /work/Sage2_Client/roll-Sage2.spec.mk install
%files kickstart
/export/profile

