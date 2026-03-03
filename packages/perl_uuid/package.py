# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install perl-uuid
#
# You can edit this file again by typing:
#
#     spack edit perl-uuid
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlUuid(PerlPackage):
    """Universally Unique Identifier library for Perl."""

    homepage = "https://metacpan.org/pod/UUID"
    url = "https://cpan.metacpan.org/authors/id/J/JR/JRM/UUID-0.36.tar.gz"

    version("0.36", sha256="c182e9ad854981a90803ae25380d2197ca6f923519e1d524bc85205eaf49bf06")
    version("0.35_02", sha256="4293c20a957b88d5f7ceb7ab315be5f5768dfc4f429d3633c9bb868faf4601fd")
    version("0.35_01", sha256="daac956bfbc65d180e5bdc85d6768675fd178f7d463bcf8ea4201953d07f5d23")
    version("0.35", sha256="41ae4884820ff29eeb3ecf542a16ef7aab687250c4956d876e9e70a88ac6dccf")
    version("0.34_02", sha256="18efd3cccaf19166fd5998aab3658373855cecdcf004841ed5671e8fd983a768")
    version("0.34", sha256="8479a34ba604103b1f3a998d4ad1c616f84e58be267ac14549f663a96badfaf0")
    version("0.33_03", sha256="33bbdbda93f7ec39552cc35eb18917cfec5b383a63128cd255b8f7533a5f65ef")
    version("0.33_02", sha256="67614ec8607ea76408923cf93b3e4e6c3f2abf56b373111bd2d08bebd4c064b5")
    version("0.33_01", sha256="7a790ddf9f5eb489f95c27d29fd87d6a3fed41cb20ea6cc3fe3db7fa239125b8")
    version("0.33", sha256="01cdb0d5a1ec31524f0cdde5167c8d35782cd93a24ba2421b12aee3ac476bf7c")
    version("0.32_14", sha256="539f1e9cc6612c4ce24fd2984db91c63c9b4de706b58017f06aec811d5055fbe")
    version("0.32_13", sha256="11ad84407f1b8ff2dec2a09233f2e77d33ee8c4e4e77ded5f0229b63788c1dd3")
    version("0.32_12", sha256="a86467077c637b0abbee6bb6fa3404bb10dce50843ab0396a9725d0219f666a0")
    version("0.32_11", sha256="4b408d57691ffa602adbcfb5d1092c095eaf9a189c9ea67ed1c0739b993fb49c")
    version("0.32_10", sha256="7aebf5555210e284e14ed17ca19556a2505f20ec7dd4589c17920f41359d3cdc")
    version("0.32_09", sha256="e0079f07029f778b2aa76004d737d77c24978d8163f315d64137404eb537f401")
    version("0.32_08", sha256="0b873f72bfeeb162342c98bcd6d5c4874e2705c75b62dd43b00356d9e26047a2")
    version("0.32_07", sha256="454c5b797adfb0d0a6f6e747d6a8bb4678abc3d900feeec2db20f125f746b2a0")
    version("0.32_06", sha256="6c2ebc3187cea2dd20d5ecd24c9e20eeb25fec4a00e19444bd652d319af4fa0b")
    version("0.32_05", sha256="d7566d29000ecd9d8993e41bb52e59a18e5193203134ec8287e577f3906e01f5")
    version("0.32_04", sha256="1d4ecca2e20c64c9e287d0184f6d88177f90f1b5e829f58707fec08f99c581b4")
    version("0.32_03", sha256="6a6be92bc95fe8cb315d8a6897ceb8c03a9335f03eb3e1b3641b8c2e3259e3cb")
    version("0.32_02", sha256="9a6cb5180aebfe07d4b08704585df86da2f61d0a868de1caafa59a3f9aebfbe4")
    version("0.32_01", sha256="ca062f483404fcb0048a1579a917740747fc836ef802369ee6bb7d3f013cd4d4")
    version("0.32", sha256="65fc07aed4dca906cf9a938c0fcfe43237a70eae00d5a411846609923fbf4da9")
    version("0.31_19", sha256="6992943614f405ad702c5d40c5f24891b347cde723ceb4ee578d61d42a957bde")
    version("0.31_18", sha256="f8fcf8263dbb36a0a3b4a5c5a6ced8b67a77bcc8bd09b9c4b16fb401a2050c13")
    version("0.31_17", sha256="44d7452cf9d9683454998fb6a0244625d874b7f9ee6dbeec6b166206a0560bab")
    version("0.31_16", sha256="44af830191d97826b41c0adac8f88b9d997ea0cf68ebad3a8d7d3314709b0163")
    version("0.31_15", sha256="9bb5def1945bc97a3bd623acee27e653d9e646a9b5fec4e2b5d44d5b0633ee94")
    version("0.31_14", sha256="abd5b4a7eccd0c31852bd6afdb9368d1c340b00e94706c9f1cfb34454f13231a")
    version("0.31_13", sha256="61f600a39e8370882dc7fbbf3e0bbbb939a5f8b0964ca2216eaa59a931871be5")
    version("0.31_12", sha256="e25310b50d533c587cdea2937c7361a64a3d7a61d8432bf9e8597d84bdc732a2")
    version("0.31_11", sha256="cbe7ab52644d2034f594adc1301ec51fa010eb6d5d55a3fc055bd9c025dc5dff")
    version("0.31_10", sha256="83064a682ecbbf5931337dafd1e214164742d6ed2a262327dffdd5069f8cc10d")
    version("0.31_09", sha256="94ba4e3cfb33db1aba809c76c736b6418c1d8c6e16e25e1e86b4a9ac26551f0e")
    version("0.31_08", sha256="1e67916d2a400379e3ea6b06c94846abff52ca112dc7aae394033025f2414ab9")
    version("0.31_07", sha256="c8f37f033233d23874906e35cc00f01477e4f6db606ce74f4c348810c6dd8d0e")
    version("0.31_06", sha256="188f65cb460fdc27c480db38e6718ef20194e8dce6694de2a9e95906c8825667")
    version("0.31_05", sha256="dc3800dfc9701935f63aa39c9177f38031abfb2a4efb4d942c6b31fd20f90903")
    version("0.31_04", sha256="013097fe5fdec05fdd90b73118b698e789ea5da0fed9f1475b960ac500a0e0ea")
    version("0.31_03", sha256="20b7abc0cc3e653626402f57d3fa2b44d8406e6514b3728b54769655f794e3f9")
    version("0.31_02", sha256="ba2d742a546e3da249eb75c7b255014c1e9924e2c5d5abd8948ccf0905fb73d6")
    version("0.31_01", sha256="4e45acc585bdcd20b088e45e0a0a9e9ad05bd7cff9ac16c32649a2c000cf1b2f")
    version("0.31", sha256="e4c0387dc535d0d64a98e5703d41eeb8cc71d34881bb6894c7a5cebd9d0673af")
    version("0.30_04", sha256="4fb2b7bc97ccb95471a68527a21efcbf9be9224f3740ac29725f8f15aac9fa91")
    version("0.30_03", sha256="2320c5d5db2f76e327295fd9205b5fcff0b015af0f860431924ce735e01805fc")
    version("0.30_02", sha256="8db7ec80dc06e63e7d4784934a26ed84e37584cf77d43cba1f2a8a822f494918")
    version("0.30_01", sha256="1eb48578a36f6ac6dd86ee2f631ac69b8dfc80f7b1815f108069b9b86ae0fbd8")
    version("0.30", sha256="00e8cb7a48731d0dbc3f89364a0507cd756a1cdef76e8030516adecfc0441909")
    version("0.29_04", sha256="68c4b5a258a8f20a92d6e6327cdc721d272111ae732835c80deca60cee08cb55")
    version("0.29_03", sha256="5de3569bcf1082232a1dbbee9ca817e3fa2622c9d4cc903b0ba6aeb23ab0563c")
    version("0.29_02", sha256="9b3ac86069928ccacca3ef94e4d622d6838fae985f6c58330e02a700067e8009")
    version("0.29_01", sha256="54576fdce0a6a7a2993303f7d52fa0a5e2ffd6366045e8fdad7d03a86eb65413")
    version("0.29", sha256="638c1f7295735af7330d153b9efc45da3ed553efe0236bed9466a2397ba546f8")
    version("0.28_01", sha256="cd0ccfce38d72ed18e6503d2eaf28befbd3db7bdcc04377665a69674954eacaf")
    version("0.28", sha256="a5c173fada973df095bd05959a3963bf24afd7fef0fd1884eff589ca8c17bb7e")
    version("0.27", sha256="ff1df2d0b0d790231166bac75b8f0c09596913fd34b765cbf0c163118353d1ef")
    version("0.26", sha256="282e3d76833c145926fc72ba08b782d9bf73c7a034b7ca32622b8940a01a8810")
    version("0.25", sha256="77e26cd58ced6cf0b7d8f0c84bfdf0de271eaef427a340989904a8e8ee268eee")
    version("0.24_03", sha256="2631c1c5cea571eac708d4cba6195ba92c1359c3bd58beea077105df135a309f")
    version("0.24_02", sha256="f01c63c41c075042259da81e9cbb1a5189b652dccc2059e991ccdf6de520e433")
    version("0.24_01", sha256="789b18d21f0052240dd80236101db1f8f123e9c9162aa143968bc5d1fe39ac3d")
    version("0.24", sha256="e57d4879c2ef5c1b5cdce732259208ee904d7f966e2efe74201da1c2181c7ca5")
    version("0.23", sha256="bca673635c518f83a4c61299c020dc1db5eb42cff58d93a1166421d10c28dd0e")
    version("0.22", sha256="74a4a574844700d565febace36f49cf88d8de6da3ef8ee9f1962969da4c8df50")
    version("0.21", sha256="bbbe7b3bdab8e75096ca8b61825b159e3394a05ea127517fa53aec16dbc86cf6")
    version("0.20", sha256="d904da11fbfbc8565ac4f61f8c141d9e71c5a625ff594606424a7808f6e14bf4")
    version("0.19", sha256="c068f7e5b6848341a0d00a4dbe6a78ab3eecb5928169af047cb925142e751d8b")
    version("0.18", sha256="1ec9dcc187be14a44986805501029cd7f4342d4ee48227bdf1375242d54e157d")
    version("0.17", sha256="c5ab341c6a278d7a2ae45508c1efe863a212321393dc6b69b38f30869aece7f3")
    version("0.16", sha256="99a7a9339a44a0728e8a8cc3cdcec051b9a945fc1c23b4f61cd18d473f2bffee")
    version("0.15", sha256="439b14ac7a0c162716ed451b70162126a61bdeb3711da2a2259d5a6bfa299468")
    version("0.14", sha256="d1c07f24ca740e43b8c1d935af189e923d336e7eeca9f5694e92aa38fd7013e3")
    version("0.13", sha256="dd0ce2001ee39a9cd4fdf6aa2fe5424a5301806716d2d322fc68dd90e532a95c")
    version("0.12", sha256="972c6850e7959ae7cb4721468e391e57d9946f9c846e12f90499a009154f93d4")
    version("0.11_01", sha256="dc086bc75b9dda378974df5acf44d1d5699531c3ae910868cedd9a25dba3494e")
    version("0.11", sha256="ec5933ae9f089109e59ed82190621a384bff98837f2c983fd96766b910818e08")
    version("0.10", sha256="e71c86aee8e6795b26bfd3bffea44d99d446cef9d2ec81fb857f8adc4d63328b")
    version("0.09", sha256="d7fcafd290ebd4268ffd799772f4cc0e71c03721aae4eda62213812c604fcada")
    version("0.08", sha256="a5d1406ea255aa933970f54ea378e9d39e1d86bbed5858a4a571260af410be1b")
    version("0.07", sha256="ef698f6996b221778267a89b8ced84c02eecc4a4ed2e3825cd94755f7e6a136b")
    version("0.06", sha256="2c0cd1aeb4c1ac1dba72994a7bd44bf95bc59230d3dd09edcc2498d831d7f686")

    depends_on("perl-devel-checklib", type="build")
