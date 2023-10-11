# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RXfun(RPackage):
    """Miscellaneous functions commonly used in other packages maintained by 'Yihui Xie'."""

    homepage = "https://github.com/yihui/xfun"
    cran = "xfun"

    version("0.40", sha256="1ea96a191a440a021b8a1414fed28cbdde5362e9b2fe95066507b535017c76f7")
    version("0.39", sha256="d0ecaabb243dd3496da6029932fcdd4772914843de7ffd0b78a172efde1356c9")
    version("0.38", sha256="a710c2f895f6c68944f38a106448f8d1e79fb0d99a5c6a3b2ee6bd8c0203c68a")
    version("0.37", sha256="3b619ff0b2aea36a1d422d1f7ca2e5cef0102e1d127c94c87acf5e6e8358e1f9")
    version("0.36", sha256="a8170de571d044eee8c852180b847b1984f8e868a9d5edd1c5e2e663171869ee")
    version("0.35", sha256="85fc4d4ea5c4266c2cd5162bf490d8c2e10fbedbf54f61fb77050437dcf1a613")
    version("0.34", sha256="50e76c1febb988c044e44fb78e1abc1ba681173c9ff3c336f4c0ad71e6a2853d")
    version("0.33", sha256="45fbc2d252867b69bbde64d4a4e3d2e049ad1d3a84984e9cfb242d8d1f41ee6c")
    version("0.32", sha256="9178c8fdea56129a96f3a15af83be9d939281dfca8e811b130446f6b7bd8865d")
    version("0.31", sha256="d169f3e682dab0c3f2ca381f2dba9b7014a5e2ca3d6863dbae3d1bca699ef235")
    version("0.30", sha256="ebf81cf302e051f0361dc4c8b519d99e20a353b4b29cee13e768663ff562c0ee")
    version("0.29", sha256="bf85bb7b4653d03e0730682ffe1d6d3544ac0b36989f9196b2054d356c224ef4")
    version("0.28", sha256="0b5be439de8bceb166d98de956eacc7c723378f8af8feef8169ca40c0a683b32")
    version("0.27", sha256="c775bf33a6bc57f8022960cbf7dc20a4e82175a9c71807b2723f46ade6805485")
    version("0.26", sha256="9e2680489b7c86794bdb1ec2fdf1bb5927120d1439f0347b09d2cfdf00d027a5")
    version("0.25", sha256="e63d7c86c8935189f5579dda4ca841adc03c4d2d92d2fd88ad4396f12f34be97")
    version("0.24", sha256="e3e39a95202f6db4f6de3a8b9a344074a4944a3a8a522d44971390c905e2b583")
    version("0.23", sha256="ec8528e85ea7e7f3dad0148359cdb0b10c8dc586bb99d4ab20b3fb24ed850e37")
    version("0.22", sha256="3e717b0eb8100f01c84e2d69c2618f9e54b801a44eef5a2ce4c030c123b8a347")
    version("0.21", sha256="648e171881e2cd14be482c15b3407bfdadbcdf7dc82a969b680223eb02d212a3")
    version("0.20", sha256="284239d12a3d5ea7d1ef8b1382fb0a7a4661af54c85510501279681871da7c10")
    version("0.19", sha256="3b027bade119637478eb25733fc6702ad8de48aa199e044e4b3cbd40e78bde97")
    version("0.18", sha256="b9b5910bcd2401870f899cc71d6889b28b4a6032211f872b258cf2a2c04a1047")
    version("0.17", sha256="b27aa14454e90facce43c255a5e04be35bc5b417ea2a1d2f0d6bfc9c43c4a5fd")
    version("0.16", sha256="4f034fb7f825ff4103241aa43a45e5aafbb72c113499cf987784d0057b38ebf4")
    version("0.15", sha256="7221a6b9c9d870c654913e11231ce84a1615733281a876c2b27f154233bfb1b9")
    version("0.14", sha256="49c121bfc95c063f2d453a1d89674f3d446bb283489d21417226844c4f336ea0")
    version("0.13", sha256="a3da8d53b74ae58bb0f121177dcf3caf312c65fc181c18f168abd59afac33e0e")
    version("0.12", sha256="ae0d3312b3642d1748a6773debb43b18d57b04f2345c562b7da1a7e8d444f069")
    version("0.11", sha256="3cc24b5a67a11204255b71e5fadbb4c303dfb34a32e79c95b787aa8997e1cc36")
    version("0.10", sha256="7b5d723faed03ced9f6f8eae23c9b2dbb23eb7d8337bacca1d042a43007cbe18")
    version("0.9", sha256="d453fe89ee39bc20f05b3bde4529182f8cd6197a221eca6b106832a28daf7cb0")
    version("0.8", sha256="c2f8ecf8b57ddec02f9be7f417d9e22fc1ae2c7db8d70aa703fc62bf4a5c5416")
    version("0.7", sha256="c9efcaf8910ad66a9594c4f7eba2d0b9051ad61c2ec01214675cef09a5f794be")
    version("0.6", sha256="a3afebf5fad5e5343ccf125b2956bc4574ec779231bdd071be09d33abdad7c88")
    version("0.5", sha256="8ba224bbf2490f7bb478fd0436592506cb98ec1fc2fc6a7ea2298344d85579f2")
    version("0.4", sha256="9bdff1d44c3a36081162e75b2680fdf03b38d51972ce90d4525937c11ef72125")
    version("0.3", sha256="897211d135a7fc5f955e4c810e0a0d8fa12b034b0a89dde47ab23e9b486b21e4")
    version("0.2", sha256="8a3ceb9dbb7efabab572429450e81a3f275b5b5ddb382fe7df6d82c49913827e")
    version("0.1", sha256="f226d4b603b04af3d1c5a8bbe9adfe06bae76aaf1ae1d04c3307f1c7eb0ba5ea")
