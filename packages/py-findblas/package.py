# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFindblas(PythonPackage):
	"""Python module for finding available BLAS libraries in the system and linking wrapped C/C++ or FORTRAN code to it"""
	
	homepage = "https://github.com/david-cortes/findblas"
	pypi = "findblas/findblas-0.1.9.tar.gz" 

	version("0.1.10", sha256="c1cfa9ce941412705a4b92bfe2585a850c5aa23d8da264f7ae8f2fd4d7cb889b")
	version("0.1.11", sha256="ee21d671a6e78749207bc1ba82cd6c4b0636b3734cc5e9b88f04bae9903c1984")
	version("0.1.12", sha256="0a57633ef352133381e1449d76799c758a66689731ef4d292ad2ae6af958ab57")
	version("0.1.13", sha256="81313878d6de28a5b5c088bbe5ffea76eaa17ba08325e63e3e73585d93dff8fb")
	version("0.1.14", sha256="0cb6e489a2768263edf10f52a3988ffd135039d73db428c3964ce72b0f8e6004")
	version("0.1.15", sha256="97c072c3eba6e2f2548e1d444cd2e25da05912533476b391dd3b00385071dc69")
	version("0.1.16", sha256="f65b1135788721ecdf29ec5ffa095ece198bc36b66c3f852d2650446e47a4d36")
	version("0.1.17", sha256="4fbbafb7656c7d64e3bae22d5e2104d7e4ef2415555b25dc5d778cf76b483d43")
	version("0.1.18", sha256="cf399c2d45bbbf9391325d975bcac492ddb56f9299c27b71c5e7d3877ba96fd0")
	version("0.1.19", sha256="5088f56c8b6aa1818466bf3f4c72d7e3eed252511d359af0fbc567b2c92cb78e")
	version("0.1.2.2", sha256="f042f85320434b2c8dd0e125cd54aab6a83198e70676bc761c80840e3e31548b")
	version("0.1.2.4", sha256="1be6b4cf6e8cebf8c9b199900c9546b3014207afa1d8e158386171e33321d032")
	version("0.1.20", sha256="26117bc515e66e34cb4cda407397cd922fa2594c99b9a14023b958af11e258a4")
	version("0.1.21", sha256="20948bd32c45ddb42be379e657e415065562f0ae01092049daa5863801b1ab5e")
	version("0.1.22", sha256="1fdb8214ab1c3122961e5e4f61f694a91e7e4a2ce3bfd1e6838e2dc46787f9b0")
	version("0.1.23", sha256="823661a9198aab3335581a19f9d9d5ad819abc7d6475278eea7b204152c2eb94")
	version("0.1.24.post1", sha256="1fa1a09aa43f1d6315dd071f582f41739b607053cad48ae77fa084a143e39272")
	version("0.1.25", sha256="191c54162d4f2c887a76a1d2649f5bee41d34628a17ce0f67ffe61dcf9670033")
	version("0.1.26", sha256="9cbe0ec275e18fe62c1b24a4cc4228d56ca953ad3825ee393db67a29926e00bd")
	version("0.1.26.post1", sha256="c8b9ca1ca063f03b5b8f3eded8eff7f13690cd043dcc5035a92f2a74ae73e7bb")
	version("0.1.3", sha256="209a647858f658eaa0ae22e32a8a0be902f30359df2f30e5b2b9da9d1d4a9c88")
	version("0.1.3.1", sha256="6326bec2a5652227ca60872c1422d7682f8fa9ba540d218ea2b7ff57b0b56a95")
	version("0.1.3.2", sha256="3ef59bd4c2d7c2c730965afbc6a628d72ec5ba55525d30328d5a99776e8d4a1b")
	version("0.1.3.3", sha256="b79d1b5003be8ff2ca65b468bd3fe9c813f445b5b2b4d9ce0844ea1302ef70a8")
	version("0.1.3.4", sha256="0fb10fa7aa98b6d792d5d2b3e75ac97e0102257a6ab593ecc146316cd45bc21a")
	version("0.1.4", sha256="d6f7ac72ecf86e9f93f6ce5a465740d1b3c4b36900ec5fec6b81d9b425d27fa6")
	version("0.1.4.2", sha256="3d773a1a716b5df747cdc5e04440691d3a7608e7f3fb1be8c764adba22478a23")
	version("0.1.5", sha256="b3fd332340a3e34c513f8b43d125ce51b62c16af68d9f8d0fbd63834ea5e4ace")
	version("0.1.5.1", sha256="a23928e5e7f2721f53aaf0609b1ae09101b64c1b8829ab2ccf05b64989fb6bee")
	version("0.1.6", sha256="ba791b0ed3c7d38c06c2365bd08098780ada3c7d65db1fe040a9f182d12d931b")
	version("0.1.7", sha256="fcfc73777bcf524244bf4cbdf7587cc1f4a517ee2b30a46ef03e7d7902f7374a")
	version("0.1.8", sha256="497ec27600ee053f3325d7aa1e9c820d8e6f2ac8b952d94757eec6c1a7f47a64")
	version("0.1.8.1", sha256="cf0af70ad22091116eb9ba6a1776c0c9fc9ff680be203e77832010b72bbcb87e")
	version("0.1.9", sha256="65ebdfc342d9f43f4e053a7f736974aed0ae23db9fbcf9008181476e1e70c58d")

	depends_on("py-setuptools", type="build")

	@run_after("install")
	def install_test(self):
		self.spec["python"].command("-c", "import findblas")
