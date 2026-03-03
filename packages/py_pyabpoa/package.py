# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyabpoa(PythonPackage):
	"""pyabpoa: SIMD-based partial order alignment using adaptive band"""
	
	homepage = "https://github.com/yangao07/abPOA"
	pypi = "pyabpoa/pyabpoa-1.5.2.tar.gz" 

	version("1.0.0a0", sha256="c8d84cedb009128a95371ec2985e1589b3d7a65f9b98f7f92fcbf53add7de840")
	version("1.0.0a1", sha256="6c80952dd834fea0d00f008f8b78e8ccb84a6f383a4424bcf318c3c05394f011")
	version("1.0.1a0", sha256="fa899ae2d3f5b83fd4ea0ce10ff2f99ceaf787d5e42728bafd0d163084c5c410")
	version("1.0.2", sha256="eb074cb663d88c1ba3a10fcbfadcc6481b4c94c15a8c593e4c59e872a6480863")
	version("1.0.3", sha256="43902d817b66b5f62685d6c7a35df1ac84a39508c211b034ce364f4682a9cca0")
	version("1.0.4", sha256="0121b549c3b199c609ff609a572975b8b60e4e1f865ceae42ae47d5045afa973")
	version("1.0.5", sha256="6788a1a336f58a2c3b2cadab5fdce154e962d975399316c9d324921a5d0f98fd")
	version("1.0.6", sha256="a57cdead39f5a5dc46d892077055dcb94bc4bd3473b03a259d0b7a67f0b92268")
	version("1.1.4", sha256="03d27a939b5bdc78e30f193b8a62488f11f3d62dce378a573a306e21e191b28d")
	version("1.2.0", sha256="cd6132c804c338ea7f60563848f195ecf3849a218b5b7c29033df1f8bf1d0bd3")
	version("1.2.1", sha256="d87cc43d1b250ba9b9722da753f790b72f9f74dd3d5e88ca40b9e0612fdb8835")
	version("1.2.3", sha256="3da878a5a839403a76e083e44f64dd556a0099464e1064b2ea1a1c7349944755")
	version("1.2.4", sha256="7619977423644aedb2d24f78d6775d86d5f1f4675c1636497439e8599b732a18")
	version("1.2.5", sha256="dff62a69280bce2dbcecdcc1b119ee2a3071a3142dc3ccda2d465bae50308f64")
	version("1.3.0.0", sha256="bbfcebe8c4fda744b88bb9fdd9041e9860d95de0a9621afe1c2960648f363b41")
	version("1.4.0", sha256="7880aff37e8fcc22cb4806ecc40628521d047df4b5aaf75b679ea82ecb24a335")
	version("1.4.2", sha256="fb35a3e8635ba5585b28d0dd0300e49eceda9a3cc97666605c335c6cbedf15cb")
	version("1.4.3", sha256="594414a069da642e2ec0a1957d4dc65ed850e698ef92879d01a46c02d202b674")
	version("1.5.0", sha256="39f27596d4f512b2a4899e9903b1acbcfc12bb95459b34d4c3c1c7aad622ad19")
	version("1.5.1", sha256="878f981e890a421d92a0d7606705d0ad9813ae6086239460dfe4b0cfc7476174")
	version("1.5.2", sha256="be39c83b12e923c9e47073cb8f0abc4c42f609fa2c0ec13d6f6a4f5a0537ee06")

	depends_on("py-setuptools", type="build")
	depends_on("zlib-api")