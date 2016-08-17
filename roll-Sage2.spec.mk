# This file is called from the generated spec file.
# It can also be used to debug rpm building.
# 	make -f roll-Sage2.spec.mk build|install

ifndef __RULES_MK
build:
	make ROOT=/work/Sage2_Client/roll-Sage2.buildroot build

install:
	make ROOT=/work/Sage2_Client/roll-Sage2.buildroot install
endif
