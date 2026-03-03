# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVegafusionPythonEmbed(PythonPackage):
    """vegafusion-python-embed PyO3 Python Package"""

    homepage = "None"
    pypi = "vegafusion-python-embed/vegafusion_python_embed-1.6.9.tar.gz"

    version("0.0.4", sha256="155530fce0a812facc6606f51cf4b2505e29f31d2d3ec29a2e58ab9968fdbb3c")
    version("0.1.0", sha256="e7b0a405cee540617f00d42b341e56a32a628cc80cdc2e460b8306174bb09b19")
    version("0.10.0", sha256="059cfb7d57d9bd49de0ceeaae98c1f65c10f77bb6967057b4a2808b599ae16c8")
    version("0.2.0", sha256="376ff73d0b02a23bc5f7b740249517ba2f8a5fef69d2430256830ba545586aea")
    version("0.3.0", sha256="cbe56204eff49b9c62a2a28289e17cbd9a89d599ecbd6f4e4f94e577030c0330")
    version("0.4.0", sha256="5ff9aaf40964f7a5f13419670ed7648f7aa6ba3eda8388196e7e1bc5add8ac0f")
    version("0.4.1", sha256="e1d7495a1dca0210b72117b70acf9fda9b00e3e255cad39ee9563033aca9925b")
    version("0.5.0", sha256="66ba1441c626631b27d5e3eb38fd4e764ef502b03031b513c45b7420d0289387")
    version("0.6.0", sha256="f408309f50a347ffd094daa1169cb153cc7d2ed9ad487dcffa6564a523731924")
    version("0.6.1", sha256="c3f80fbd89ed562e613d71bbd56876598f66383f3592e84ec8cac599cb2f512d")
    version("0.6.2", sha256="89ab33e4a65e809112dd7b9eb85ff797b8a467bb3514477c108c9f2eddf613d9")
    version("0.7.0", sha256="d9c102ed720f600c5040a3741d2ce235f6274d00e79d2e2b2491dc8e2d05b617")
    version("0.8.0", sha256="def965d2284adaf471840c48aa05b4d13de018708a714d13130bcf63adaa2228")
    version("0.9.0", sha256="98bb03e52bdfd2c90b95d936c8bb89c2c68a1c210849d596acc6f6f6b369bb44")
    version("1.0.0", sha256="a178dead3e676f701e5e0ea5df988811590f675d62d75cbcf6380aa45120dc05")
    version("1.0.1", sha256="e36d87b2be3fc2ef00cba91210ea1d38bec320c64346462eb6762bbaba4589bf")
    version("1.0.2", sha256="7b6c0ea09bf1babb44c0aff127e9c43a5d2554b951dfbfc49465f80921de4397")
    version("1.0.3", sha256="8eb80750ca9a6603403f45282c57e16c35bd2e3bd872cba74452f0642a048ba7")
    version("1.0.4", sha256="aeb90b1703c3cd64c34718aea4c067b1dcd631c1308a0429301b5ef1d16bbb09")
    version("1.1.0", sha256="22daee47e7adbe59e90e9385e78e1628728007af5123ba677f18df25a177ba15")
    version("1.1.1", sha256="191113670ded494bc4c6139f5d4a05a21fb2ed366aa622a57d6ca6c6e2050d12")
    version("1.1.2", sha256="5cda83ef8ec3b3c861d8d50470e8748887ce1f1b23848e7686042979a53ec3ff")
    version("1.1.3", sha256="8cbd5b98ccc3043fe25750aa9179f744c6e35adedc2577d47ae4979bc6690f82")
    version("1.2.0", sha256="066576cf5ae2df165ed6599cbc6f7dede425190e887113e40cff821c7cbde057")
    version("1.2.1", sha256="4ff97706e071233230eaf61cf0ac49a27805b03dcf5ee1a53a7f5207cd9311b4")
    version("1.2.2", sha256="3c2824487aab337d23a4849376410a0469d5c32d7d810d15d79ca76ac506acf5")
    version("1.2.3", sha256="00cc171ec2ab7a8b4de290289f086c3a3e0b125afb81c5d91d646c661f81598e")
    version("1.2.4", sha256="1ad54f6b15da83d7215df30dadde9bb488264542073bb5915ebc189d40381fcb")
    version("1.3.0", sha256="b20dc788d22b18898ad5925542b087e009452ffef75c01aa2e3b9a61dd0bd21f")
    version("1.3.0rc1", sha256="2a70ff73f6c8617386dbee4135ef462db62e18c111f03151a5cac0662d8ca279")
    version("1.3.0rc2", sha256="bf45c7b8b01da350dbe1496a13f3bd29193a634bdcaafc5d6c4e6821fb0197ab")
    version("1.3.0rc3", sha256="4af94e6023e8aec8027925da29987a15241f6252465303583a9b121921dba558")
    version("1.3.0rc4", sha256="6ae9a82df0e64109c4496301e428f6876ce50c8b0c72e08be20425489252ba1a")
    version("1.4.0", sha256="2a7d34e2e3e1c890e7d7893fc1d0e873859a596ce6096e5428714189108d46a9")
    version("1.4.0rc1", sha256="4363833564d6ee61582d795f3d31c43699eca818e769087744e80a926d0dce73")
    version("1.4.1", sha256="8ec624b537a42f6daa7eb04820cfdd6c51fd8614f0ab5590097280f549ae837a")
    version("1.4.2", sha256="1d2a4fe9b8afefc7cb679a830e6ceb77514da7128c3740d0c4c00603ede9f17b")
    version("1.4.3", sha256="355aa9d6503fd2575c92caed5ae21c2e8e116cb3ff241b0a677503c448db71d9")
    version("1.4.4", sha256="9119e3bf0229c9a0bb79f6eb2f56dbbbbcd5e6828028ab77a5bd179ff6dd867a")
    version("1.4.5", sha256="ae45d0c1277f0908ce58ca9e06ba995dea150b15036b92aeec5991ff2947b66e")
    version("1.5.0", sha256="21063271ee89eab64eb0baf7035cc859ebf42107d7b9417c523b8b7da2531460")
    version("1.5.1", sha256="362a263734e7efd2a362ec2d4a7765d450ef7201b15313a63f20e3b38579bb86")
    version("1.6.0", sha256="c5797c33c261d83f161079eef49feced9cfc7a8b66dd0aac11e3548378dc2054")
    version("1.6.0rc1", sha256="957553f77de97a49212f74be526c28725e9a150f5523f5342c52eee33db44adf")
    version("1.6.1", sha256="4965998f536faff5ba9ac6633bd78345519a50790f1798c5c4f653124d0b609d")
    version("1.6.2", sha256="22262c3064105fab1d7a4108ad4bce7e8156d5036994c19c01faf98029a430d0")
    version("1.6.3", sha256="9f77b5b24bfa19f7f2f2f011fbc9a3a1a6138941cafd9c9257e86921d3e21b25")
    version("1.6.4", sha256="d96747c1e5959d323912b76ec2e7fbd5687363f4fd34f42ac888bbade8ede840")
    version("1.6.4rc1", sha256="ef7f69a435bc5396f6de6e025d3f8d6983ee56401347de0a9de45513c944e0cc")
    version("1.6.5", sha256="04e06ee98fe99afd3fb206cdd98a42cbfd5922785e19cb3cd2e1efcb7dccab77")
    version("1.6.6", sha256="840ecce7f160f12c08101b5129388eeeb0e8859e303f33c6371bad2cce7ceb1e")
    version("1.6.7", sha256="f37d80fccf5ad6f3dd49dbb972a293e3c134229bf421e3faff62572778e8e14e")
    version("1.6.8", sha256="f67aaf32e0b7969c8b70a47167dddfc9e68b941631e054497adc4cfea21c51dd")
    version("1.6.9", sha256="6e339c236c8a15e59898cb4ab490ab3ca40af4657db588d8d766fc1f2ba80c20")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-maturin", type="build")
    depends_on("protobuf", type="build")
