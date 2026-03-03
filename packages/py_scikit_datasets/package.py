# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitDatasets(PythonPackage):
	"""Scikit-learn-compatible datasets"""
	
	homepage = "https://github.com/daviddiazvico/scikit-datasets"
	pypi = "scikit-datasets/scikit_datasets-0.2.5-py3-none-any.whl" 

	version("0.1.10", sha256="c0eb951549ba2a03978f910f5126f3260a6f86704e65a3959f9ab6a1978a3dc9", expand=False, url="https://files.pythonhosted.org/packages/5a/9e/73f60dc7ce0f5243a3876291cb116e204f19b59e4ece1b4779eb8d703b84/scikit_datasets-0.1.10-py3-none-any.whl")
	version("0.1.11", sha256="9cdd32e808af858b63de56c397ecba9284903f7d215166643c0cd02c07f424ce", expand=False, url="https://files.pythonhosted.org/packages/b6/79/ddb937180a88f5e8fe1325fee585aa18b4c1cec3032443cac07329b160c8/scikit_datasets-0.1.11-py3-none-any.whl")
	version("0.1.12", sha256="1449f0d1c0bdb774eaf563d3a8111e1b5879be6c1d86a394707146c5a02cdb63", expand=False, url="https://files.pythonhosted.org/packages/b9/02/0c33aeb3f9b83fb12dfab4619ba8111e072adab0be907f25667cfdcdd2ec/scikit_datasets-0.1.12-py3-none-any.whl")
	version("0.1.13", sha256="4375db0bc34e03ec912a2f26b91e04cf236c20e853bb5a6e997f6360303a513b", expand=False, url="https://files.pythonhosted.org/packages/bd/a4/abc51e5cc6309609c22fbf65322ab481f74e42f1f1fab1fe3b53727de31c/scikit_datasets-0.1.13-py3-none-any.whl")
	version("0.1.14", sha256="bbe11c11370446546a6724d5b3a012bf375642e8d5b16e66b3ce92e25d665e33", expand=False, url="https://files.pythonhosted.org/packages/62/e8/d56d6a1468e36da4e9ff752cd431d71d9ef086bf7215b254bc54b142aabd/scikit_datasets-0.1.14-py3-none-any.whl")
	version("0.1.15", sha256="4467a45762587688854c1b14ca95fd747223bbc4515f30e8bd3de01709a9f47e", expand=False, url="https://files.pythonhosted.org/packages/76/68/2721f35f9c77201135391da958bd1d86fa56dbb2c5616f5e0db08a889d90/scikit_datasets-0.1.15-py3-none-any.whl")
	version("0.1.16", sha256="592fd9f38fb6bb6954f30369fcccfadd226faea501642d108f22b43c552b2fa5", expand=False, url="https://files.pythonhosted.org/packages/d2/56/2c418912d8ba462f49b128f27fbfc42248da77faaf685c7c244bc9c1e706/scikit_datasets-0.1.16-py3-none-any.whl")
	version("0.1.17", sha256="5acb6a1d0c2fc3125b88651882d186368b851d99421dc2974ef3817d2e13b697", expand=False, url="https://files.pythonhosted.org/packages/62/62/a68c7e532f7c5aa5db97d5b8c12be8d5ae1b90ebbbf2d9d932948025bb0d/scikit_datasets-0.1.17-py3-none-any.whl")
	version("0.1.18", sha256="61f6aba4a639aa2d66c0b43c0011c0425db9dfea989a7bfeeb5cf7e4039727e3", expand=False, url="https://files.pythonhosted.org/packages/cb/05/5305900decdc270afb06972a0f335adbce6cdc94b978216e37307a22e846/scikit_datasets-0.1.18-py3-none-any.whl")
	version("0.1.19", sha256="56e85b2706815db1f22affa7645fd3cd3e593b1be82ca4b04edbf2321de7141e", expand=False, url="https://files.pythonhosted.org/packages/35/46/f7d0c18c6ce23b57630280ad1ebe3732abf02098aac5954eff441befd3ff/scikit_datasets-0.1.19-py3-none-any.whl")
	version("0.1.2", sha256="db072b9ee0f267acd516a47c63a250719ddfa9def209eeed23a5d94d0531c0ae")
	version("0.1.21", sha256="6ce425ca803a57e18880af04c120fdf17313068b24b4b6be5d5c1e8cf78bea1e", expand=False, url="https://files.pythonhosted.org/packages/d8/9f/d98c74c81691976ae76e5bfcb44e8e3cd3ac861e28a4459a6eefc6d82470/scikit_datasets-0.1.21-py3-none-any.whl")
	version("0.1.22", sha256="99e93d0dc473affc749b284b8ea40a1ae54983aba0779f7a64dcbb8289c4aa53", expand=False, url="https://files.pythonhosted.org/packages/16/95/1b29f2ceeee4b489d8839b48588eb45036a316988c13fbc07c110ca7065f/scikit_datasets-0.1.22-py3-none-any.whl")
	version("0.1.23", sha256="1899a22895457ef32410b8a934c16e43de909ecec7525bab1e7b2d19784636aa", expand=False, url="https://files.pythonhosted.org/packages/2e/11/5b0989e016631fb37b7df78a9a5d3036608fd581f9a50bc800f51f94e2c3/scikit_datasets-0.1.23-py3-none-any.whl")
	version("0.1.24", sha256="e4ae15b23aed70d62ba58ad854a18830c2a35ba6f183c01472c4b930a63a005c", expand=False, url="https://files.pythonhosted.org/packages/34/13/28d97f425ad9020b16bc17b4d0c7b1cedf0dcd75734122d9d0e526b64e40/scikit_datasets-0.1.24-py3-none-any.whl")
	version("0.1.25", sha256="5c7ef671d0c45306472684b73dceb411349f0b608b16758ebb9ff27705ec1d35", expand=False, url="https://files.pythonhosted.org/packages/36/85/3f9a18536a08d7d33b14c06b3c523559dd33b58fcb534b28a37c3558519f/scikit_datasets-0.1.25-py3-none-any.whl")
	version("0.1.26", sha256="f68453a0f25e7851b214dde8a9ffd764f967b6da3120e1d22d26b7d8077998fc", expand=False, url="https://files.pythonhosted.org/packages/7f/ad/d90d4882261711a6886bfbede942ea3947d774c776857dd95f579cd60fb0/scikit_datasets-0.1.26-py3-none-any.whl")
	version("0.1.27", sha256="97545a947b672f1a246258677a4944e9bff239b2bff54bd0b1f217b9b27a7a03", expand=False, url="https://files.pythonhosted.org/packages/f3/02/2a04ac346c9d0a8d07cebb17fac352fae15e86859b4fa571619bb3a9a051/scikit_datasets-0.1.27-py3-none-any.whl")
	version("0.1.28", sha256="86149c1776c5c92b4d8583523567e53c157bf9d5f6d62c97039094bbd6cc9219", expand=False, url="https://files.pythonhosted.org/packages/a4/ca/6cffc827e634dbb0ff5e72a9ec3dade1d8c2b6a43fc81fb6dea92614e6b1/scikit_datasets-0.1.28-py3-none-any.whl")
	version("0.1.29", sha256="147ffabe3bb21926827a6f571a29713fe35d96f2b1ac18ccbb203df684d434c8", expand=False, url="https://files.pythonhosted.org/packages/4e/25/86642bdb312c07a69e6478e9e1329f362ee5f62eb2d7bb9dab932b62f7fe/scikit_datasets-0.1.29-py3-none-any.whl")
	version("0.1.3", sha256="cac1f8833d7f02fa21bb6cb3257282bb23af3c35b56eae3d50b2482be47a6f5d")
	version("0.1.30", sha256="1578c2bdaa208ded9846173e6613a274b043d0d698277f7a3194fd074c7a2a74", expand=False, url="https://files.pythonhosted.org/packages/48/7d/4d30c3802d2ae83bb038060a47f1ebb9a19cb25ce60987f32622ef312099/scikit_datasets-0.1.30-py3-none-any.whl")
	version("0.1.31", sha256="f485a7f294a4ba8cba03bd308c8313319469f134bdedaa112e054e86cd3ae5ae", expand=False, url="https://files.pythonhosted.org/packages/db/a9/b0e6d6e16945a5c099176a74b440b38531261e2834295b2d53033ea9dafe/scikit_datasets-0.1.31-py3-none-any.whl")
	version("0.1.32", sha256="42ea66ee24a38173367661727261987c14617542694b382af81f9e0cc1598bd0", expand=False, url="https://files.pythonhosted.org/packages/12/4b/2311f51fa3ae40ca492751dc80236af20f46f4cec234ec01124711c2db96/scikit_datasets-0.1.32-py3-none-any.whl")
	version("0.1.33", sha256="491887ce8a65965c48114a25bc487593056e40843c0190077bc17df06e705a1a", expand=False, url="https://files.pythonhosted.org/packages/da/c6/ed0cb45302fbca84cdd125457c1e9ba6901d9f996eb15e380792ffd0b239/scikit_datasets-0.1.33-py3-none-any.whl")
	version("0.1.34", sha256="289ba408d8e80249cbde4ede0f87957174255e4a63543f9e94d3dd0bfa0e2c12", expand=False, url="https://files.pythonhosted.org/packages/e2/59/b1307a8472d69f3bba18a4d10463bcee820ab8561e06ccaa556f7dfab04d/scikit_datasets-0.1.34-py3-none-any.whl")
	version("0.1.35", sha256="2897f351cd1739e4c31d8a21a3343e066d04214e9715fbb869dfd36f6d7a855c", expand=False, url="https://files.pythonhosted.org/packages/26/33/8612d2f001ba58a8d4e637dd3bb6c64fd372267be32da55af3c20abbbc93/scikit_datasets-0.1.35-py3-none-any.whl")
	version("0.1.36", sha256="19a6b074e92039d3bc4548af2ebee26ac71ccb06cfbb037e2c33bbb0455c73b1", expand=False, url="https://files.pythonhosted.org/packages/89/f1/858de12daffb183c368412425905d4b6e0fdda4d9d119dd2158123d2fdaa/scikit_datasets-0.1.36-py3-none-any.whl")
	version("0.1.37", sha256="1301955e655a9c2bedbd48955f4c3685d4083a7c7bd6bc0f1a801269e3c887f0", expand=False, url="https://files.pythonhosted.org/packages/48/1a/5180f40fa4cc1625cbb64ae7c7a9bed1619f6e91571c14aa575ccfae5192/scikit_datasets-0.1.37-py3-none-any.whl")
	version("0.1.38", sha256="79218fe053e7a408426805acafcfe5400978c390e8043e49931354ef15fda801", expand=False, url="https://files.pythonhosted.org/packages/33/e2/cd885185aa16351eb962ca06d68e0d1887d963fd2842b51db9193a26d7bc/scikit_datasets-0.1.38-py3-none-any.whl")
	version("0.1.4", sha256="9c88e147a0b2f24f39b3bc1c33454bc3d9da97511d3712e5b798873726511138")
	version("0.1.5", sha256="3dc9891a9e3f7546b2781d53be11aa629359647958cc3e873dcdaa879101a48c")
	version("0.1.6", sha256="09750eb7ee530dc26c180cca0211d42271f858e9749b1f7085112ba1a80dd8b5")
	version("0.1.7", sha256="ce39564e192f18604b9d63aebe3830f5935d49d947e908b0c44be85fcbcf25cd")
	version("0.1.8", sha256="2a5606ccd08c8b2f9b155cef7fc2610e4df2dff93b5dfaa16b0980729d9dc562")
	version("0.2.0", sha256="3813342f32eb38b9657f44db31c1d74a5e5d69e5c29645b5027cf186269e6381", expand=False, url="https://files.pythonhosted.org/packages/ff/a7/e4e566e2dad128acac80182fcb97fb5fe1636cb3ac8ae495efeed39451c1/scikit_datasets-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="0934056c61c1d66f891a83b78b8ec55d1883e4cc32f7cfb7cc30a367f2ee7d3f", expand=False, url="https://files.pythonhosted.org/packages/a9/01/fe12d005cf58ace8e5cbccacc164602b24c75607a03b45f8812983c75a4f/scikit_datasets-0.2.1-py3-none-any.whl")
	version("0.2.2", sha256="28c469a435523529dfc6a3fb1db2f854a31dd712280f75be8828acfc8de17e20", expand=False, url="https://files.pythonhosted.org/packages/d0/54/155ecbc198f5fdd26956f0c44431797b2bb4dbb98e1bf1c4b1aa930b6bc4/scikit_datasets-0.2.2-py3-none-any.whl")
	version("0.2.3", sha256="2fef0b2e2f99c010a3869de51cd9c04388c0e0546d87e7c8291d948522167035", expand=False, url="https://files.pythonhosted.org/packages/19/d0/62d4d49804f7946a44fdc4b0e1114e8be6a4a700f95046ba89e26f2636a5/scikit_datasets-0.2.3-py3-none-any.whl")
	version("0.2.4", sha256="96eb9c2bf377a4e7b545d6a9397e8e9fa157b151f8c01e94cdb2ee25f7e1f018", expand=False, url="https://files.pythonhosted.org/packages/d3/f2/a826a6cbac91dba8f656ba88e5b97c7ff467cb43a079e4331b83802e4d37/scikit_datasets-0.2.4-py3-none-any.whl")
	version("0.2.5", sha256="63b2977866704a2014f9327bde573231468dfd461ed1d75844d4a9b19bddb60a", expand=False, url="https://files.pythonhosted.org/packages/0f/d7/0cc33111166455d7b992225db9fe3c82fc99eef9ab9d34ce6eac51472ce3/scikit_datasets-0.2.5-py3-none-any.whl")

	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))

	@run_after("install")
	def install_test(self):
		self.spec["python"].command("-c", "import skdatasets")
