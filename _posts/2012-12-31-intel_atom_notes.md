---
title: "Intel Atom notes"
date: 2012-12-31 12:38:13 +0000
categories: ["PhD", "smart meters"]
permalink: /intel_atom_notes
---
Current preferred spec
======================

### Case & PSU

-   Item:
    [Cypher](http://www.akasa.com.tw/update.php?tpl=product/product.detail.tpl&no=181&type=Chassis&type_sub=Mini%20ITX&model=AK-ITX04-BK#)
    AK-ITX-04BK Mini-ITX from Akasa with 120W PSU VESA Mountable
-   Manufacturer: Akasa
-   Description: Small computer case
-   Supplier: scan
-   Supplier product code: LN45102
-   Web page:
    http://www.scan.co.uk/products/akasa-cypher-ultra-compact-mini-itx-case-black-with-120w-psu
-   Number required: one
-   Price (ex VAT): £44.98

This case has a "brick" PSU which should work with the 12V power input
on the DN2800MT motherboard. Lovely small case. Has a hole for an RP-SMA
connector (antenna). Just about enough space to mount a Nanode SMT
inside.

The plug on the PSU which comes with the case is too big to fit the
mobo. The mobo needs a "8 - 19 VDC external power supply though the DC
jack on the back panel. This connector accepts dualbarrel plugs with an
inner diameter (ID) of 2.5 mm and an outer diameter (OD) of 5.5 mm,
where the inner contact is +8 (±10%) through +19 (±10%) VDC and the
shell is GND. The maximum current rating for this connector is 8 A."
(from p58 of the mobo manual.) So it's necessary to chop off the HUGE
connector on the PSU (which has an outer diameter of about 7mm and an
inner diameter of about 5mm) and replace it with:

-   Item: CONN PWR PLUG DC 2.5X5.5 8A MOD
-   Manufacturer: CUI Inc
-   Description: DC plug with 5.5mm OD, 2.5mm ID, 14mm length (and
    locking groove? TBC)
-   Supplier: Digi-Key
-   Supplier product code: CP3-002BH-ND
-   Web page:
    http://www.digikey.co.uk/scripts/DKSearch/dksus.dll?Detail&itemSeq=127910444&uq=634992759972123594
-   Number required: 6
-   Price (ex VAT): 1.30

### Motherboard

-   Item: Intel DN2800MT Atom motherboard
-   Manufacturer: Intel
-   Description: mini-ITX motherboard with built-in Atom CPU
-   Supplier: Scan
-   Supplier product code: LN43166
-   Web page:
    http://www.scan.co.uk/products/intel-boxdn2800mt-mini-itx-intel-atom-n2800-motherboard-ddr3-1066-so-dimm
-   Number required:
-   Price (ex VAT): £66.28

(also available from [Micom](http://www.micom.co.uk/intel-dn2800mt))

The N2800 Atom has enhanced speed step so should be capable of consuming
just a few watts. It uses a PowerVR GPU which has virtually no Linux
support. But that's not a problem because it'll be a headless data
logger..

-   Item: 2GB (1x2GB) DDR3 1066Mhz Value Select SODIMM 204 Pin Notebook
    Memory Module
-   Manufacturer: Corsair
-   Description: Memory module
-   Supplier: BT Business Direct
-   Supplier product code: 5GK8QE00
-   Web page:
    [www.businessdirect.bt.com/products/corsair-2gb--1x2gb--ddr3-1066mhz--value-select-sodimm--204-pin-notebook-memory-module-5GK8.html](www.businessdirect.bt.com/products/corsair-2gb--1x2gb--ddr3-1066mhz--value-select-sodimm--204-pin-notebook-memory-module-5GK8.html)
-   Number required: one
-   Price (ex VAT): £6.66

### WiFi

-   Item: U.FL-RPSMA BULKHEAD MOUNT, 200MM
-   Manufacturer: GIGATRONIX
-   Description: Antenna cable
-   Supplier: Farnell
-   Supplier product code: 1706348
-   Web page:
    http://uk.farnell.com/gigatronix/u-fl-rpsmabulk-200mm/u-fl-rpsma-bulkhead-mount-200mm/dp/1706348
-   Number required: one
-   Price (ex VAT): £6.42

Cheaper cables are available from Amazon but I need to use a
college-approved supplier. Farnell 2143312 would also be a cheaper
option (£3.50) but wasn't in stock when I ordered.

-   Item: RN-SMA4-RP - ANTENNA, 2.4GHZ, 4INCH W/ RPSMA
-   Manufacturer: MICROCHIP
-   Description: WiFi antenna
-   Supplier: Farnell
-   Supplier product code: 2143322
-   Web page:
    http://uk.farnell.com/microchip/rn-sma4-rp/antenna-2-4ghz-4inch-w-rpsma/dp/2143322?Ntt=2143322
-   Number required: one
-   Price (ex VAT): £4.08

-   Item: Centrino Wireless-N 2230

-   Manufacturer: Intel
-   Description: mini PCIe wireless network card
-   Supplier: Micom
-   Supplier product code: 2230BN.HMWWB
-   Web page: http://www.micom.co.uk/intel-centrino-wireless-n-2230
-   Number required: 5
-   Price (ex VAT): £11.65

This plugs into the motherboard. It's designed to use two antennae but
it seems to work fine with one antenna on my 802.11g network. There are
[lots of Intel miniPCIe
adapters](http://ark.intel.com/products/family/30656). Some have draft-N
support only. Some have Bluetooth (which I don't need). Cheaper adapters
can be found on Google but this 6230 adapter is fairly cheap and comes
from an approved supplier; plus Intel WiFi adapters should have good
support on Linux. Insight also do the WiFi Link 1000 and Wireless-N 1030
(both for £9.99 ex VAT) but these are "order upon request".

### Hard drive

-   Item: Seagate Momentus 320GB 5400.5 2.5" Notebook Hard Drive
-   Manufacturer: Seagate
-   Description: Hard disk drive
-   Supplier: Scan
-   Supplier product code: LN26698
-   Web page:
    http://www.scan.co.uk/products/320gb-seagate-st9320325as-momentus-54005-25-95-mm-sata-3gb-s-5400rpm-8mb-cache-14ms-ncq
-   Number required: one
-   Price (ex VAT): £28.32

The system draws \~14W while logging (but with a power factor of only
about 0.35)

Build order:
------------

-   Take top off case
-   Remove HDD bracket
-   Fit back plate
-   Fit motherboard
-   Fit WiFi aerial cable
-   Fit WiFi mini PCIe card & connect to aerial cable
-   Fit cables from case to motherboard
-   Fit HDD to bracket and install in case and fit cables

Additional notes
================

Electronics
-----------

-   Item: HEADER, RIGHT ANGLE, 6WAY
-   Manufacturer: TE CONNECTIVITY / AMP
-   Description:
-   Supplier: Farnell
-   Supplier product code: 1248172
-   Web page:
    http://uk.farnell.com/te-connectivity-amp/826947-6/header-right-angle-6way/dp/1248172
-   Number required: six
-   Price (ex VAT): £0.199

The header is required because the header supplied on the NanodeRF SMT
isn't right-angled, so the FTDI adapter sits at right angles to the
Nanode, and this configuration won't fit in the tiny Atom case. So we
need to replace the straight header with a right-angled header.

-   Item:
-   Manufacturer:
-   Description:
-   Supplier:
-   Supplier product code:
-   Web page:
-   Number required:
-   Price (ex VAT):

Motherboards
============

D945GSE
-------

-   [Tech specs
    PDF](http://www.intel.com/support/motherboards/desktop/d945gsejt/sb/CS-030300.htm)
-   Min power draw = 12.28 W
-   Max power draw = 42.01 W
-   Audio is ICH7-M with ALC662 audio codec
-   "Front panel audio header with support for Intel High Def Audio"
-   NO LINE IN (see table 4 on p21 of tech spec PDF)
-   N270 (2.5W TDP)

continued... <!--break-->

D2700MUD
--------

-   [Tech
    specs](http://www.intel.com/support/motherboards/desktop/d2700mud/sb/CS-032620.htm)
-   [£57 inc VAT on
    eBuyer](www.ebuyer.com/318725-desktop-board-d2700-2-13ghz-1m-box-boxd2700mud)
-   Min power draw = 23 W
-   Max power draw = 88 W
-   Atom D2700 (no enhanced speed step. speed step doesn't appear to be
    available at all in Linux on this CPU)
-   Two SO-DIMM slots for 1066/800 MHz DDR3 single-channel memory
-   SATA 2.0 Gb/s
-   VGA and DVI-D ports
-   Audio Intel NM10 and Realtek ALC662
-   Line in is definitely supported. Not clear if second line in also
    supported???

D525-based boards
-----------------

-   Has much better Linux support for GMA
-   But appears to have no CPU freq throttling support on Linux
    (or Windows?)

Audio
=====

Realtek ALC662 audio codec
--------------------------

-   [tech
    specs](http://www.realtek.com.tw/products/productsView.aspx?Langid=1&PFid=37&Level=5&Conn=4&ProdID=144)
-   two stereo ADCs, 16/20-bit PCM format, 44.1k/48k/96kHz sample rate
-   All analog jack port are stereo input and output re-tasking
-   Up to four channels of microphone array input are supported for
    AEC/BF application

Complete PCs
============

There are lots of "nettop" PCs which are very cost effective. But
finding one with an N2800 Atom (with enhanced speed step), audio
line-in, and just enough space to install a Nanode inside, and a
padlockable-case is tricky (although it's a little ambiguous whether the
mic-in ports on these nettop PCs can be re-programmed to be line-in
ports). The Lenovo Q180 is impressive.

http://www.ebuyer.com/store/Computer/cat/Nettop

[LGX AG150](http://www.logicsupply.com/blog/2012/03/08/low-profile-high-octane-computing-with-the-lgx-ag150/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+logicsupply%2Fblog+%28Logic+Supply+Blog%29)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   1.86 GHz N2800
-   fanless
-   expensive!

Misc notes on college-approved suppliers
========================================

misco
-----

-   has nice mini-ITX cases with silent PSU but only usable if I can
    find mobo with WiFi
    http://www.misco.co.uk/Product/162779/Akasa-Crypto-Compact-Mini-ITX-Case-60Watt
-   has no Atom mobos
-   has cases of a similar form factor to the one I have

BT
--

-   several thin-client Akasa cases
-   one mini ITX case which claims to accept 1 expansion board:
    <http://www.businessdirect.bt.com/products/antec-isk-310-150-mini-itx-desktop-7370.html?refs=44080000>
-   only old Atom mobos. And only "ordered upon request"

MICOM
-----

-   one expensive (£62 ex VAT) Atom motherboard:
    http://www.micom.co.uk/intel-dn2800mt
-   does have a Gigabyte GA-C847N
    http://www.micom.co.uk/gigabyte-ga-c847n-motherboard
-   several cases eg: \*\* http://www.micom.co.uk/aopen-s135b (60W
    silent PSU. don't think this will take an expansion card though)
    \*\* Antex ISK 310-150 http://www.micom.co.uk/antec-isk-310-150 (1
    half-height expansion card) \*\*
    http://www.micom.co.uk/cooler-master-elite-120-advanced \*\*
    http://www.micom.co.uk/aopen-h340a
-   Zotac ZBOX SD ID12 Barebone PC Intel Atom Dual Core (D525) £117 ex
    VAT

SCAN
----

-   Akasa Cypher mini ITx with 120W PSU and what looks like an SMA hole
    £44.98 ex VAT
    http://www.scan.co.uk/products/akasa-cypher-ultra-compact-mini-itx-case-black-with-120w-psu
-   http://www.scan.co.uk/products/akasa-euler-ak-itx-05bkal-mini-itx-for-intel-dq77kb-ivy-bridge-intel-dh61ag-sandy-bridge-motherboard
-   several cases with DC PSUs (not what we want)
-   Nice Zotac NM10-E-E Atom D525 mobo with wifi for £70 ex VAT but
    pre-order
-   Nice Zotac NM10-F-E Atom D525 with wifi for £60 ex VAT but pre-order
-   Mede8er wirless mini pcie card with aerial £24.89 ex VAT
    http://www.scan.co.uk/products/mede8er-med20pcie-wireless-n-minipcie-upgrade-5db-kit


