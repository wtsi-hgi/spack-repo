# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPeppy(PythonPackage):
	"""A python-based project metadata manager for portable encapsulated projects"""
	
	homepage = "https://github.com/pepkit/peppy/"
	pypi = "peppy/peppy-0.9.0.tar.gz" 

	version("0.17.0", sha256="8cf7ff821e248cc08cc29456f5557aa75f17772584f63d87859e344c86a6be81")
	version("0.17.1", sha256="95bed61b7d54c81469098876b3ff8b8ad189a20a449a518d941924f03191596f")
	version("0.17.2", sha256="a572ac096654bc2dfec2f63e1c53a5b538117bd58f73b198e0777966f32da97a")
	version("0.18.0", sha256="dee27874b003849aa06b7c65f605970f87dad7101519ab9e4d9001564fab7c7d")
	version("0.18.1", sha256="a39b89e5508c97602f158122e85f9c89e7996a83c46b9b2bf8fabd8ef303bc56")
	version("0.18.2", sha256="6c6f4393d1457faa8d3dfcb10b5c8bd0404f11f55f58af7a885b1e1990e1fb12")
	version("0.19", sha256="f2589ba08933e1ec6c3de111915a6b9f7581f1fff935cd0b5febd2498ea79491")
	version("0.19.1", sha256="7081b10843c5495ab1a82e9402d59ee9efce3e6de82f7f90ebe0d2cc5e1c0765")
	version("0.20", sha256="891f56111b8af8e47f2e306ec540ec87ac1426dafd9caa5ebffe42508a681e64")
	version("0.21.0", sha256="c2c170feae3ff3bf3c981fe8fe28e88886841a863192e1e35f39849db5a54a9c")
	version("0.22.0", sha256="4d4cfa84cd7ec6c884ad7145ac1e68ae34ff07574cfb92aad366195bac65de71")
	version("0.22.1", sha256="6f4b7dd40c2be5ec36225d622628f94d4c300c9f1c08ee86fd42d25e3c6a00f5")
	version("0.22.2", sha256="5ab12efc7729dfd2fbef5f0d70ada6df93f3d956c7df48009f1a84f79b877a1f")
	version("0.22.3", sha256="e4933f8cdbabdba35e7c2a376962e2e4a8a7c884831248b054376ca257462b73")
	version("0.30.0", sha256="76fa4042966fb60d81ca95db9218035937bd871953ce1252c478351ad313c1fc")
	version("0.30.1", sha256="058703fd51eeb5dfb57f0dd2bc24ff11c7d999773f43787d76628138697992aa")
	version("0.30.2", sha256="56c08532efd928726e6d6ca28aeb14efe8ea6603fb4abce31400b9a026cd653c", expand=False, url="https://files.pythonhosted.org/packages/6e/8b/72f39bf710fc5bcccd72f556806ea02a774c584bf3f607de958df968775f/peppy-0.30.2-py3-none-any.whl")
	version("0.30.3", sha256="d50a3659820a59644f95a1ba5a36e38043c8c94ac4d4479d2922702ae0a7c0fc", expand=False, url="https://files.pythonhosted.org/packages/44/a1/c81dade2b32b5b4b1256f61fd54943794366dc428c6e325c4ff98fe9dfd2/peppy-0.30.3-py3-none-any.whl")
	version("0.31.0", sha256="6e8ca214a1bde0eac2c17563aadfa233bea09115eb14b434215101d1aa419313", expand=False, url="https://files.pythonhosted.org/packages/27/01/41f64f1c719f6bbe27d706eeb73b4fb9d1d05e2cd3253676a11450dddc54/peppy-0.31.0-py3-none-any.whl")
	version("0.31.1", sha256="1810242911fcfe19d308d96f65296968152f01e93c1f15211c361924946bfcad", expand=False, url="https://files.pythonhosted.org/packages/19/6d/0d64be46aaa043db7124d70bbd6e9ecf46926f5f692d9e59f7ac0058d672/peppy-0.31.1-py3-none-any.whl")
	version("0.31.2", sha256="f26fc9a4ba55bb803d7e7249a1db50b27bb7d9f83bc2072b7a1d8849af5a6478", expand=False, url="https://files.pythonhosted.org/packages/a3/61/c65c1c3116e6d393c9e0203f2fa1465e53cb2b899412d6a940257678ae61/peppy-0.31.2-py3-none-any.whl")
	version("0.32.0", sha256="20758ae5113b16c1a963ef89bf90f31d016f1159b6ee4b69d7d95ad751317dd1", expand=False, url="https://files.pythonhosted.org/packages/9f/e8/6408917780ad77fab727bab814c0a278c60c061b21780c024b5c43bc81d0/peppy-0.32.0-py3-none-any.whl")
	version("0.33.0", sha256="4a3914604e6ca3ca1272d827b7ced2baf517a996cd9c5f41caacd15240cd0ffd", expand=False, url="https://files.pythonhosted.org/packages/68/2a/e2427ef8dec33873d4d0d979554cc0c0b6d930efe30cba7d709c9c129095/peppy-0.33.0-py3-none-any.whl")
	version("0.34.0", sha256="48bbcdc6f425525976f234864f3eebadba12cf531500a505d16a9d748e2e82c8", expand=False, url="https://files.pythonhosted.org/packages/49/10/42b4a82de436bdca3159c1db596f4e6aca89b9e5291ffa6172c786777b9d/peppy-0.34.0-py3-none-any.whl")
	version("0.35.0", sha256="13efe8df44606256819a6190c7fa6398bca9c32c966c7ddf49bf792c8a364deb", expand=False, url="https://files.pythonhosted.org/packages/1b/9b/81e31c2d1c72e3107acd50702ff5389ff47740ac9e32a08724dea4137651/peppy-0.35.0-py3-none-any.whl")
	version("0.35.1", sha256="dd9e99930773f5c7c6ddbc3de7f1a7f9387627be8bd80e255d6158fb63781f1a", expand=False, url="https://files.pythonhosted.org/packages/80/af/47beaf531e269e1be1ab4bc1d52c3cc1f009822f26fd54452768334ee951/peppy-0.35.1-py3-none-any.whl")
	version("0.35.2", sha256="b1f993358eb4c4b4e317cf41142f0db24a8743afcf48e8294acfec739d925687", expand=False, url="https://files.pythonhosted.org/packages/52/fe/79c3fc6608227e37e0cb01ac5cf62b5931a37910a5c42f8aa61c58d7d85f/peppy-0.35.2-py3-none-any.whl")
	version("0.35.3", sha256="63a832e113d9ad3f09cc086e3ad1fe041cbf88a30b91ecbfb19175c49a4797de", expand=False, url="https://files.pythonhosted.org/packages/49/f1/8fa700079393cdba4f6d76743017b704420abf8d2a7ce352efa9987b895c/peppy-0.35.3-py3-none-any.whl")
	version("0.35.4", sha256="88c0e3e450b1a5ce96f6dd7b39be25749e4742dd45a34488841d64abd03f666f", expand=False, url="https://files.pythonhosted.org/packages/c4/60/a1d3a437f8cd69432b214cd8cd67b296ff29ad2680e27834a41d75eaaed6/peppy-0.35.4-py3-none-any.whl")
	version("0.35.5", sha256="1e9b14c9182c2d1fd90fda832347ddbe6ccaa6a0db087a01be12e5aedc62e4f8", expand=False, url="https://files.pythonhosted.org/packages/14/28/75f98028431c9988eb1e2bf742eaeb35bd771917ba70f36a0bb9b78f8962/peppy-0.35.5-py3-none-any.whl")
	version("0.35.6", sha256="654637c37e0185879dfcb51c013324d07b9e612d5920f5692d08407b77a3c592", expand=False, url="https://files.pythonhosted.org/packages/e6/cc/e51d0acdafb9f2c124a636345dd9762c8123f41870d5f7a68568b91b3d9c/peppy-0.35.6-py3-none-any.whl")
	version("0.35.7", sha256="b675df5027160b98fd87e5a3ba7ac65b90cf9aafa8acfa678006c74bcb1b39ef", expand=False, url="https://files.pythonhosted.org/packages/a4/39/22b984ff419fafd3315dbc0c23c12099d15dd8e0e7099c337f8097e5d4ec/peppy-0.35.7-py3-none-any.whl")
	version("0.40.0", sha256="965d86a0c38d231527ad419424c4375471722f05c06b9c99823b397f85a36a66", expand=False, url="https://files.pythonhosted.org/packages/2e/a9/c5c7e5b39e776cf0fe0140f9157498acab5d174f0152a76a61e884119573/peppy-0.40.0-py3-none-any.whl")
	version("0.40.0a1", sha256="a46b4630e70ec30af490f7f727e9b5d1e2d564510863c62d2ee750e5a377609a", expand=False, url="https://files.pythonhosted.org/packages/6d/bb/a9967ebffcd10ac6594eb2602d340eabb9720ec2b68ec6e6fd149854c7d5/peppy-0.40.0a1-py3-none-any.whl")
	version("0.40.0a2", sha256="23f98dbfca87fa27421d4af52c12e93e57378a8a288118b3dfd68d7a7603aa42", expand=False, url="https://files.pythonhosted.org/packages/6b/e6/8ceded98a2f5d2b192b3e8a709e2444ec48f58c79bba6122d4cff48d4392/peppy-0.40.0a2-py3-none-any.whl")
	version("0.40.0a3", sha256="f2ff1a36fd2f6b728c62ac456afea95f444b550ce09b6fb347e36f75c2c24d07", expand=False, url="https://files.pythonhosted.org/packages/67/cb/4b0c806d5aa79f8c1766d7e2fc07f9e0981222bebe3cbd09750b16a2b3af/peppy-0.40.0a3-py3-none-any.whl")
	version("0.40.0a4", sha256="c1ce297f8ef02288851502b98b7f6e5eba9dc10028b8afc5da76a251a60135b6", expand=False, url="https://files.pythonhosted.org/packages/65/f6/658ad4242df9c11ba02c1313ff6f1fcbc246011fc1b1acdec63af82bb3b9/peppy-0.40.0a4-py3-none-any.whl")
	version("0.40.0a5", sha256="af53570649f18236cc2d760ba299f4ae1e340efd48fb5bde1eb3605c585ac90d", expand=False, url="https://files.pythonhosted.org/packages/21/d6/19311ef5fbfa80f88a8744fdb38a6ed39008925fd261cae5455f5d92de4a/peppy-0.40.0a5-py3-none-any.whl")
	version("0.40.1", sha256="33cfa369e26cb785d3a7e6d6a6036fe7d1d29b53073f2d497cd269c6fa7945fb", expand=False, url="https://files.pythonhosted.org/packages/00/4f/1f284acbe44d319d9c79dfd862ea01ee25f31f6fd3568ec89a83176d3c8b/peppy-0.40.1-py3-none-any.whl")
	version("0.40.2", sha256="b038c8a7a06160d87787c6e7b6904c56be97ac7c8bbdda5c0d7b6f59e9db2876", expand=False, url="https://files.pythonhosted.org/packages/c9/0a/0f758361eeafe0c7a620ba6266fd81a8ea990f02c1d2106d2a387fa20d3d/peppy-0.40.2-py3-none-any.whl")
	version("0.40.3", sha256="0aa3df9b37cd2ac35e769469a0fd431434ee786ecc0b74d5f1748c09c04aa979", expand=False, url="https://files.pythonhosted.org/packages/94/5b/5b9ef25641cd16aba675a8c107f291259becdc36de8a500ee347256072ae/peppy-0.40.3-py3-none-any.whl")
	version("0.40.4", sha256="461053a47727a26b384a2a42f4cb6c6930f22ecad827d380ca0b4624aa4b1afc", expand=False, url="https://files.pythonhosted.org/packages/4b/ee/cbbc42679f9da29450a3fe873e449d9064abe426a2f07bb2bb102a0b0ce0/peppy-0.40.4-py3-none-any.whl")
	version("0.40.5", sha256="2dc7d4390e608c0362eec0329b3798c0824a3a20e4f9aaa2625862835a7e5378", expand=False, url="https://files.pythonhosted.org/packages/ce/1a/30f539365d29e21a1c0eaa9ed4b6c82b7ea75937d3eb4295e42c59c29c64/peppy-0.40.5-py3-none-any.whl")
	version("0.40.6", sha256="b951ef560571800a4ccf68c856c9579dde981ef19e3243ba5bf3efe181d69784", expand=False, url="https://files.pythonhosted.org/packages/f9/fd/34de0bf9686863e057b1c9eff7ca208564318b7cb3223a12a9ce7deb9251/peppy-0.40.6-py3-none-any.whl")
	version("0.40.7", sha256="5d2351f6cee6172eb82b90149b931a7827ed0445965b23ba3c36ddb70b3c2b3e", expand=False, url="https://files.pythonhosted.org/packages/8b/c7/101211791373b6e7d5aae3c34815e92493e61263ef52215ab7fd96cd6b31/peppy-0.40.7-py3-none-any.whl")
	version("0.9.0", sha256="eb03e6788717e732eda9d7b8d029aa0eae1606caa7a70bf43de8ad789aa878a7")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-pyyaml", type=("build", "run"))
	depends_on("py-rich", type=("build", "run"))
	depends_on("py-ubiquerg", type=("build", "run"))
# {'attmap(>=0.12.5)': ['0.30.2', '0.30.3', '0.31.0', '0.31.1'], 'pandas(>=0.24.2)': ['0.30.2', '0.30.3', '0.31.0', '0.31.1', '0.31.2', '0.32.0', '0.33.0', '0.34.0', '0.35.0', '0.35.1', '0.35.2', '0.35.3', '0.35.4', '0.35.5', '0.35.6', '0.35.7', '0.40.0a1'], 'pyyaml(>=5)': ['0.30.2', '0.30.3', '0.31.0'], 'logmuse(>=0.2)': ['0.30.2', '0.30.3', '0.31.0', '0.31.1', '0.31.2', '0.32.0', '0.33.0', '0.34.0', '0.35.0', '0.35.1', '0.35.2', '0.35.3', '0.35.4'], 'ubiquerg(>=0.5.2)': ['0.30.2', '0.30.3', '0.31.0', '0.31.1'], 'pyyaml': ['0.31.1', '0.31.2', '0.32.0', '0.33.0', '0.34.0', '0.35.0', '0.35.1', '0.35.2', '0.35.3', '0.35.4', '0.35.5', '0.35.6', '0.35.7', '0.40.0', '0.40.0a1', '0.40.0a2', '0.40.0a3', '0.40.0a4', '0.40.0a5', '0.40.1', '0.40.2', '0.40.3', '0.40.4', '0.40.5', '0.40.6', '0.40.7'], 'attmap(>=0.13.2)': ['0.31.2', '0.32.0', '0.33.0', '0.34.0', '0.35.0', '0.35.1', '0.35.2', '0.35.3', '0.35.4', '0.35.5', '0.35.6', '0.35.7'], 'ubiquerg(>=0.6.2)': ['0.31.2', '0.32.0', '0.33.0', '0.34.0', '0.35.0', '0.35.1', '0.35.2', '0.35.3', '0.35.4', '0.35.5', '0.35.6', '0.35.7', '0.40.0a1'], 'rich(>=10.3.0)': ['0.32.0', '0.33.0', '0.34.0', '0.35.0', '0.35.1', '0.35.2', '0.35.3', '0.35.4', '0.35.5', '0.35.6', '0.35.7', '0.40.0a1'], 'pandas>=0.24.2': ['0.40.0', '0.40.0a2', '0.40.0a3', '0.40.0a4', '0.40.0a5', '0.40.1', '0.40.2', '0.40.3', '0.40.4', '0.40.5', '0.40.6', '0.40.7'], 'rich>=10.3.0': ['0.40.0', '0.40.0a2', '0.40.0a3', '0.40.0a4', '0.40.0a5', '0.40.1', '0.40.2', '0.40.3', '0.40.4', '0.40.5', '0.40.6', '0.40.7'], 'ubiquerg>=0.6.2': ['0.40.0', '0.40.0a2', '0.40.0a3', '0.40.0a4', '0.40.0a5', '0.40.1', '0.40.2', '0.40.3', '0.40.4', '0.40.5', '0.40.6', '0.40.7'], 'numpy': ['0.40.0', '0.40.1', '0.40.2', '0.40.3', '0.40.4', '0.40.5', '0.40.6', '0.40.7'], 'yacman(>=0.9.0)': ['0.40.0a1'], 'yacman>=0.9.0': ['0.40.0a2', '0.40.0a3', '0.40.0a4', '0.40.0a5'], 'pephubclient>=0.4.2': ['0.40.3', '0.40.4', '0.40.5', '0.40.6', '0.40.7']}