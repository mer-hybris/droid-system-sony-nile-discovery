%define multiple_rpms 1
%define rpm_device discovery

%define dsd_path ./

Requires(post): coreutils
Requires(post): libcap

%include droid-system-device/droid-system.inc

# rest of this file is autogenerated. do not edit
%post
[ -e /system/bin ] && chown 0:2000 /system/bin
[ -e /system/bin/adbd ] && chown 0:2000 /system/bin/adbd
[ -e /system/bin/am ] && chown 0:2000 /system/bin/am
[ -e /system/bin/app_process32 ] && chown 0:2000 /system/bin/app_process32
[ -e /system/bin/app_process64 ] && chown 0:2000 /system/bin/app_process64
[ -e /system/bin/applypatch ] && chown 0:2000 /system/bin/applypatch
[ -e /system/bin/appops ] && chown 0:2000 /system/bin/appops
[ -e /system/bin/appwidget ] && chown 0:2000 /system/bin/appwidget
[ -e /system/bin/atrace ] && chown 0:2000 /system/bin/atrace
[ -e /system/bin/audioserver ] && chown 0:2000 /system/bin/audioserver
[ -e /system/bin/bcc ] && chown 0:2000 /system/bin/bcc
[ -e /system/bin/blkid ] && chown 0:2000 /system/bin/blkid
[ -e /system/bin/bmgr ] && chown 0:2000 /system/bin/bmgr
[ -e /system/bin/bootanimation ] && chown 0:2000 /system/bin/bootanimation
[ -e /system/bin/bootstat ] && chown 0:2000 /system/bin/bootstat
[ -e /system/bin/bu ] && chown 0:2000 /system/bin/bu
[ -e /system/bin/bugreport ] && chown 0:2000 /system/bin/bugreport
[ -e /system/bin/bugreportz ] && chown 0:2000 /system/bin/bugreportz
[ -e /system/bin/bzip2 ] && chown 0:2000 /system/bin/bzip2
[ -e /system/bin/cameraserver ] && chown 0:2000 /system/bin/cameraserver
[ -e /system/bin/clatd ] && chown 0:2000 /system/bin/clatd
[ -e /system/bin/cmd ] && chown 0:2000 /system/bin/cmd
[ -e /system/bin/content ] && chown 0:2000 /system/bin/content
[ -e /system/bin/crash_dump32 ] && chown 0:2000 /system/bin/crash_dump32
[ -e /system/bin/crash_dump64 ] && chown 0:2000 /system/bin/crash_dump64
[ -e /system/bin/dalvikvm32 ] && chown 0:2000 /system/bin/dalvikvm32
[ -e /system/bin/dalvikvm64 ] && chown 0:2000 /system/bin/dalvikvm64
[ -e /system/bin/debuggerd ] && chown 0:2000 /system/bin/debuggerd
[ -e /system/bin/dex2oat ] && chown 0:2000 /system/bin/dex2oat
[ -e /system/bin/dexdiag ] && chown 0:2000 /system/bin/dexdiag
[ -e /system/bin/dexdump ] && chown 0:2000 /system/bin/dexdump
[ -e /system/bin/dexlist ] && chown 0:2000 /system/bin/dexlist
[ -e /system/bin/dexoptanalyzer ] && chown 0:2000 /system/bin/dexoptanalyzer
[ -e /system/bin/dnsmasq ] && chown 0:2000 /system/bin/dnsmasq
[ -e /system/bin/dpm ] && chown 0:2000 /system/bin/dpm
[ -e /system/bin/drmserver ] && chown 0:2000 /system/bin/drmserver
[ -e /system/bin/dumpstate ] && chown 0:2000 /system/bin/dumpstate
[ -e /system/bin/dumpsys ] && chown 0:2000 /system/bin/dumpsys
[ -e /system/bin/e2fsck ] && chown 0:2000 /system/bin/e2fsck
[ -e /system/bin/e2fsdroid ] && chown 0:2000 /system/bin/e2fsdroid
[ -e /system/bin/fsck.f2fs ] && chown 0:2000 /system/bin/fsck.f2fs
[ -e /system/bin/fsck_msdos ] && chown 0:2000 /system/bin/fsck_msdos
[ -e /system/bin/gatekeeperd ] && chown 0:2000 /system/bin/gatekeeperd
[ -e /system/bin/grep ] && chown 0:2000 /system/bin/grep
[ -e /system/bin/healthd ] && chown 0:2000 /system/bin/healthd
[ -e /system/bin/hid ] && chown 0:2000 /system/bin/hid
[ -e /system/bin/hw ] && chown 0:2000 /system/bin/hw
[ -e /system/bin/hw/android.hidl.allocator@1.0-service ] && chown 0:2000 /system/bin/hw/android.hidl.allocator@1.0-service
[ -e /system/bin/hwservicemanager ] && chown 0:2000 /system/bin/hwservicemanager
[ -e /system/bin/idmap ] && chown 0:2000 /system/bin/idmap
[ -e /system/bin/ime ] && chown 0:2000 /system/bin/ime
[ -e /system/bin/incident ] && chown 0:2000 /system/bin/incident
[ -e /system/bin/incidentd ] && chown 0:2000 /system/bin/incidentd
[ -e /system/bin/input ] && chown 0:2000 /system/bin/input
[ -e /system/bin/installd ] && chown 0:2000 /system/bin/installd
[ -e /system/bin/ip ] && chown 0:2000 /system/bin/ip
[ -e /system/bin/ip6tables ] && chown 0:2000 /system/bin/ip6tables
[ -e /system/bin/iptables ] && chown 0:2000 /system/bin/iptables
[ -e /system/bin/keystore ] && chown 0:2000 /system/bin/keystore
[ -e /system/bin/ld.mc ] && chown 0:2000 /system/bin/ld.mc
[ -e /system/bin/linker ] && chown 0:2000 /system/bin/linker
[ -e /system/bin/linker64 ] && chown 0:2000 /system/bin/linker64
[ -e /system/bin/lmkd ] && chown 0:2000 /system/bin/lmkd
[ -e /system/bin/locksettings ] && chown 0:2000 /system/bin/locksettings
[ -e /system/bin/logcat ] && chown 0:2000 /system/bin/logcat
[ -e /system/bin/logd ] && chown 1036:1036 /system/bin/logd
[ -e /system/bin/logwrapper ] && chown 0:2000 /system/bin/logwrapper
[ -e /system/bin/lshal ] && chown 0:2000 /system/bin/lshal
[ -e /system/bin/make_ext4fs ] && chown 0:2000 /system/bin/make_ext4fs
[ -e /system/bin/make_f2fs ] && chown 0:2000 /system/bin/make_f2fs
[ -e /system/bin/mdnsd ] && chown 0:2000 /system/bin/mdnsd
[ -e /system/bin/media ] && chown 0:2000 /system/bin/media
[ -e /system/bin/mediadrmserver ] && chown 0:2000 /system/bin/mediadrmserver
[ -e /system/bin/mediaextractor ] && chown 0:2000 /system/bin/mediaextractor
[ -e /system/bin/mediametrics ] && chown 0:2000 /system/bin/mediametrics
[ -e /system/bin/mediaserver ] && chown 0:2000 /system/bin/mediaserver
[ -e /system/bin/mke2fs ] && chown 0:2000 /system/bin/mke2fs
[ -e /system/bin/monkey ] && chown 0:2000 /system/bin/monkey
[ -e /system/bin/mtpd ] && chown 0:2000 /system/bin/mtpd
[ -e /system/bin/ndc ] && chown 0:2000 /system/bin/ndc
[ -e /system/bin/netd ] && chown 0:2000 /system/bin/netd
[ -e /system/bin/netutils-wrapper-1.0 ] && chown 0:2000 /system/bin/netutils-wrapper-1.0
[ -e /system/bin/oatdump ] && chown 0:2000 /system/bin/oatdump
[ -e /system/bin/otapreopt ] && chown 0:2000 /system/bin/otapreopt
[ -e /system/bin/otapreopt_chroot ] && chown 0:2000 /system/bin/otapreopt_chroot
[ -e /system/bin/otapreopt_script ] && chown 0:2000 /system/bin/otapreopt_script
[ -e /system/bin/otapreopt_slot ] && chown 0:2000 /system/bin/otapreopt_slot
[ -e /system/bin/patchoat ] && chown 0:2000 /system/bin/patchoat
[ -e /system/bin/ping ] && chown 0:2000 /system/bin/ping
[ -e /system/bin/ping6 ] && chown 0:2000 /system/bin/ping6
[ -e /system/bin/pm ] && chown 0:2000 /system/bin/pm
[ -e /system/bin/pppd ] && chown 0:2000 /system/bin/pppd
[ -e /system/bin/profman ] && chown 0:2000 /system/bin/profman
[ -e /system/bin/racoon ] && chown 0:2000 /system/bin/racoon
[ -e /system/bin/reboot ] && chown 0:2000 /system/bin/reboot
[ -e /system/bin/recovery-persist ] && chown 0:2000 /system/bin/recovery-persist
[ -e /system/bin/recovery-refresh ] && chown 0:2000 /system/bin/recovery-refresh
[ -e /system/bin/requestsync ] && chown 0:2000 /system/bin/requestsync
[ -e /system/bin/resize2fs ] && chown 0:2000 /system/bin/resize2fs
[ -e /system/bin/run-as ] && chown 0:2000 /system/bin/run-as
[ -e /system/bin/schedtest ] && chown 0:2000 /system/bin/schedtest
[ -e /system/bin/screencap ] && chown 0:2000 /system/bin/screencap
[ -e /system/bin/screenrecord ] && chown 0:2000 /system/bin/screenrecord
[ -e /system/bin/sdcard ] && chown 0:2000 /system/bin/sdcard
[ -e /system/bin/secdiscard ] && chown 0:2000 /system/bin/secdiscard
[ -e /system/bin/sensorservice ] && chown 0:2000 /system/bin/sensorservice
[ -e /system/bin/service ] && chown 0:2000 /system/bin/service
[ -e /system/bin/servicemanager ] && chown 0:2000 /system/bin/servicemanager
[ -e /system/bin/settings ] && chown 0:2000 /system/bin/settings
[ -e /system/bin/sgdisk ] && chown 0:2000 /system/bin/sgdisk
[ -e /system/bin/sh ] && chown 0:2000 /system/bin/sh
[ -e /system/bin/sm ] && chown 0:2000 /system/bin/sm
[ -e /system/bin/storaged ] && chown 0:2000 /system/bin/storaged
[ -e /system/bin/surfaceflinger ] && chown 1000:1003 /system/bin/surfaceflinger
[ -e /system/bin/svc ] && chown 0:2000 /system/bin/svc
[ -e /system/bin/tc ] && chown 0:2000 /system/bin/tc
[ -e /system/bin/telecom ] && chown 0:2000 /system/bin/telecom
[ -e /system/bin/thermalserviced ] && chown 0:2000 /system/bin/thermalserviced
[ -e /system/bin/timekeep ] && chown 0:2000 /system/bin/timekeep
[ -e /system/bin/tinymix ] && chown 0:2000 /system/bin/tinymix
[ -e /system/bin/tombstoned ] && chown 0:2000 /system/bin/tombstoned
[ -e /system/bin/toolbox ] && chown 0:2000 /system/bin/toolbox
[ -e /system/bin/toybox ] && chown 0:2000 /system/bin/toybox
[ -e /system/bin/tune2fs ] && chown 0:2000 /system/bin/tune2fs
[ -e /system/bin/tzdatacheck ] && chown 0:2000 /system/bin/tzdatacheck
[ -e /system/bin/uiautomator ] && chown 0:2000 /system/bin/uiautomator
[ -e /system/bin/update_engine ] && chown 0:2000 /system/bin/update_engine
[ -e /system/bin/update_engine_client ] && chown 0:2000 /system/bin/update_engine_client
[ -e /system/bin/update_verifier ] && chown 0:2000 /system/bin/update_verifier
[ -e /system/bin/vdc ] && chown 0:2000 /system/bin/vdc
[ -e /system/bin/vold ] && chown 0:2000 /system/bin/vold
[ -e /system/bin/vr ] && chown 0:2000 /system/bin/vr
[ -e /system/bin/wificond ] && chown 0:2000 /system/bin/wificond
[ -e /system/bin/wm ] && chown 0:2000 /system/bin/wm
[ -e /system/./bin/logd ] && setcap cap_setgid,cap_audit_control,cap_syslog+ep /system/./bin/logd
[ -e /system/./bin/run-as ] && setcap cap_setgid,cap_setuid+ep /system/./bin/run-as
[ -e /system/./bin/surfaceflinger ] && setcap cap_sys_nice+ep /system/./bin/surfaceflinger
[ -e /system/./bin/webview_zygote32 ] && setcap cap_setgid,cap_setuid,cap_setpcap+ep /system/./bin/webview_zygote32
[ -e /system/./bin/webview_zygote64 ] && setcap cap_setgid,cap_setuid,cap_setpcap+ep /system/./bin/webview_zygote64
