# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTensorstore(PythonPackage):
	"""Read and write large, multi-dimensional arrays"""
	
	homepage = "https://github.com/google/tensorstore"
	pypi = "tensorstore/tensorstore-0.1.9.tar.gz" 

	version("0.1.0", sha256="c72a76aabe04efbc0417ac01dc2117891557cb9b8387aade6a9f5ca1f8beb20a")
	version("0.1.1", sha256="c0c0a98d52d9dd9cd4274b8fbd92d6f9051f7c1e9d2bf3f90e705950267bc1f3")
	version("0.1.10", sha256="ff8b8be2b0e53b52d2b1f5fc912f5503b8cccb8e2c9c6256952c20c5edb14945")
	version("0.1.11", sha256="2abea879b1961bc6db1367a9e2a757f1ed64fd5c6bb0364ed50a06f0d34061af")
	version("0.1.12", sha256="320e960eab509ab29b96a3ef40b11ac8e4049f4f731c8fe1b3eecf8351274d59")
	version("0.1.13", sha256="4f3f87c02a047e0b14eac356cde2e384feaaef30de48a9cecb8324b9eecaf30b")
	version("0.1.14", sha256="a5df0d88fd86b15609da20d41cb7d715df2364354dd83681e32ab4f1ff25f903")
	version("0.1.15", sha256="59b8436e3a9b93914f86cf79589f2e7a1fc89fbc5bf9cb94f064e7f05ab51a30")
	version("0.1.16", sha256="436d12fd6245108bb9477f30c1b3e18b407e36571f2919f7a7f13761f184fbed")
	version("0.1.17", sha256="a3bf3272fb49f1b34f3a7bacb091f577e6524b006d81e31a90e2f221541b2646")
	version("0.1.18", sha256="3ac3ccdc6e0450e71c63d3d6e548efec0ebd28f07ec0ed77838a9626cbc05ea8")
	version("0.1.19", sha256="a23565502ab63c1bac886ed3e4a8f0cf27230a29a5a87884d9234f64fa5295a8")
	version("0.1.2", sha256="1dae0e054cf3de009752562f9722d2917f015294363493ff3e558d4f44ee8a16")
	version("0.1.20", sha256="c4421fcee56d402dadada6f5ff56c6736789234b432b774887eecf1f029f8b10")
	version("0.1.21", sha256="c620c3b06e1606092bd444bb7687c9d5a8049e8ed5f4c17ee0fd53e0a43b7df7")
	version("0.1.22", sha256="a90ab2b40b635ed4e15a1f9af9d34b7901e5c58506c5d50e80aebd6850d0b700")
	version("0.1.23", sha256="63931f74346970ff6b79fd803b008760129217d231b1173ed77fb66b319490ef")
	version("0.1.24", sha256="4284c988991a49c286f6de82594bff98a1fe89aa092febf84e0501f6e5561d73")
	version("0.1.25", sha256="16cd53365d95b85f4863459e34506b28f499ee5227c6849965512aa8d99ccac3")
	version("0.1.26", sha256="418a9edd454d30c0bde5bd15dcc5f2649daee5c602f0cfbc50ab9f939fb1a294")
	version("0.1.27", sha256="73f1d3cf7d6e6f92c482bcc3ff1a59dbff9194652d15bc9fd1164dbb6578dac5")
	version("0.1.28", sha256="cd8d8185136632c58edcd7cf4c43d301bf8ad61a197c632cb495d7d33b7be04e")
	version("0.1.3", sha256="09fadc0388d3c247a130d4135ad7b340780a898890c5ada5d04fdee802d8c293")
	version("0.1.30", sha256="b46612fdddf51267c0ffc88666283c0675e196180572912233af781040533475")
	version("0.1.31", sha256="8529b7ab2dedf80f5d3e0e88f70203f7387fab443d95347de01538c6fc9f77a6")
	version("0.1.32", sha256="497470cc199aa1d115e90be1d0e88208acb84dccae7d1e5a967fad4cd9f144c8")
	version("0.1.33", sha256="471d449b9dcbfe5f08691ccf95f3b61188d8306540dd6112d9a689f8c3b6f6e8")
	version("0.1.35", sha256="93db16e2f448cad716628640d3b73b87d9b259ae8ba1741a82108aef14e427c6")
	version("0.1.36", sha256="733b629a65f1d47cc1b19fb1df2de75111ae228081655746d335ed3c21902bbd")
	version("0.1.37", sha256="70e8ba35da96cf45c1298140881df3d1532fe7ec01091bb64eb944085d0406ee")
	version("0.1.38", sha256="61400782073a190d7be51c5cf39819b9974a9ad607c830d393ed796a9814fd27")
	version("0.1.39", sha256="ccee5ebd1ccaeaba4e36186702eae31513813c001d9c84cfd6aadd7821075602")
	version("0.1.4", sha256="ad0f1237668f813baa09e419fe1e9a1adc1cb2b0e3eb08f8ecc8ad2dac6ce88f")
	version("0.1.40", sha256="41517dbd3919e5a5ee2be69b51bdd528b57c9b35f533e6fc83f6155a378fdf8a")
	version("0.1.41", sha256="5168f7f71e51da7d6cc85a11cd5d102d9eae750d5f5a3ee90cc9ebae10226621")
	version("0.1.42", sha256="1526bc2d437edf52cf5bcfcbd4af10163478e7512897b1c86395245e46eca62a")
	version("0.1.43", sha256="7914eb6f5e53bcf20aa62d8b86df73b85c794a902d3875de4474e80b6ac78168")
	version("0.1.44", sha256="4c95d23c8cfd60ab9e3b109728f49e3b41fa699de33fd54495c0976573cfec27")
	version("0.1.45", sha256="38468c621b2edf09cfdd2df4905890e83f1805c7645ec13e16df5eafabf0e5e5")
	version("0.1.46", sha256="b5074a67919ebf89da1e794f88f87dc0d19f98f4ce7b484a083f7422c83cf9de")
	version("0.1.47", sha256="734c8bdf63ced1d0d45ef008da4f4b54cebcedcac1a20cf255d5cf7679abd3ee")
	version("0.1.48", sha256="cf07a75aaa84098cf7b4d673485a326cde1695101225a04bc7b557fcc3c2cbb7")
	version("0.1.49", sha256="b0dc120ca4c4bcbb3ec28d826f56d3995fd47e375908f936662f0f7653859515")
	version("0.1.5", sha256="c3e2740e307653679a1e14e3453e5aa8653338932ba5d69b2ac0630141d389ac")
	version("0.1.50", sha256="e251226bfaca7829966e78712156df316137257328001d3295df849be577e61f")
	version("0.1.51", sha256="8a7610c0cc5263593dd8865160f7a1c51d8380706008cd0f866150b36550bd31")
	version("0.1.52", sha256="db2130a8b792ee2f1fb74a4e89ea049ecbb0070370d365d91870822cbf6cfca7")
	version("0.1.53", sha256="45ef74b2dc9f2cd5f766bc373ded91d681cd021cc69d16592df48abaeb81af56")
	version("0.1.54", sha256="e1a9dcb0be7c828f752375409537d4b39c658dd6c6a0873fe21a24a556ec0e2a")
	version("0.1.55", sha256="ccdcceb507223d25b121d4cb15e94339948cfb9bbe08be77e972db0d74fc5485")
	version("0.1.56", sha256="5f8f7bc056cb15bc0d45fedfe1ec38029d6f361aa2fb155a218a577a6d953013")
	version("0.1.6", sha256="32dcc8564ea80a6174812162b2baeec5253235d57021c88c64d634b0e44dd498")
	version("0.1.7", sha256="bfb40e990da067bffcef79893fb187e82f67561557045b00ef70e8768d4fa7ab")
	version("0.1.8", sha256="2956928a3e18f79d7586227b68a4f8fe7363dbb40abcab3cc236e96be1a61ffb")
	version("0.1.9", sha256="10570375efea50e672eca9cc0d01d109f864a6aa0e3def10cd7b6c1cc4ef76e6")

	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-ml-dtypes", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-setuptools", type="build")
	#depends_on("abseil-cpp", type=("build", "link"))
	#depends_on("bazel", type=("build", "link"))

	def setup_build_environment(self, env):
		env.set("CC", self.compiler.cc)
		#env.set("CXX", self.compiler.cxx)
