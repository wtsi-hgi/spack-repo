# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitPosthocs(PythonPackage):
	"""Statistical post-hoc analysis and outlier detection algorithms"""
	
	homepage = "https://github.com/maximtrp/scikit-posthocs"
	pypi = "scikit-posthocs/scikit_posthocs-0.9.1-py3-none-any.whl" 

	version("0.10.0", sha256="0fa1d4640cf2d1d5a602ed7be3848a4ce54f426f179a7df9ae7a5787f94455c1", expand=False, url="https://files.pythonhosted.org/packages/ee/94/6fcc320ed6e8025d493aaf92295986d6d4bee2071ebda466bc39cd13d903/scikit_posthocs-0.10.0-py3-none-any.whl")
	version("0.11.0", sha256="168e98c33fbdc32c34c31c83b0578c0c9e2242f24724bbe69427df3a8682bec0", expand=False, url="https://files.pythonhosted.org/packages/d1/1b/b42beacbc465368c30d68454ec7bbdb82bfceaacf75454dae053d8fcad20/scikit_posthocs-0.11.0-py3-none-any.whl")
	version("0.11.1", sha256="7fa2e42611c78cec6d08c542e90507d15d4e7bd578fc585af19cec2080a19b89", expand=False, url="https://files.pythonhosted.org/packages/45/cb/f88201de5658f17588618d96208715141b9ce7452ca6ae485f4bf71b8f81/scikit_posthocs-0.11.1-py3-none-any.whl")
	version("0.11.2", sha256="adaa21547c2e3c34eec9d86d6a06e379552a187c87bc06e2b71e9f00cf57b86a", expand=False, url="https://files.pythonhosted.org/packages/e5/0c/99f0d7552fcaf295b60fcb9117e5772d0f7ea9c36ded488c5352a6383be8/scikit_posthocs-0.11.2-py3-none-any.whl")
	version("0.11.3", sha256="c20f98c3c51ed3ce9b0bce58d2405bc6bc9c20c72dd95586c1e70ca39081f3f7", expand=False, url="https://files.pythonhosted.org/packages/32/58/146847070f723e099eaf12df287bd6d62f7fc8e0f9e131a1932a9ab3c56c/scikit_posthocs-0.11.3-py3-none-any.whl")
	version("0.11.4", sha256="9c8447c2983c36cb943d6798ba0aab03fe76c16b36d966bd8c14f2e5b29d90cc", expand=False, url="https://files.pythonhosted.org/packages/d6/21/506f0ab734ad73f9215b09e04a05b393170c391349778f0c676a7b88cb7a/scikit_posthocs-0.11.4-py3-none-any.whl")
	version("0.3.4", sha256="b17f54fe09bad978dc7acfadefb7fcaa22b601dc6524fbbe8c5c4e1668f9de6a", expand=False, url="https://files.pythonhosted.org/packages/e6/cd/fe35e09c6b05e37d4c377025c55e6c45d75a5266a2e245a4fcd5f93609dd/scikit_posthocs-0.3.4-py2.py3-none-any.whl")
	version("0.3.6", sha256="e9d57253bc2ed47d3ca7300ed4f409af061fe3461b7aa2d7f7125d3614f512cc", expand=False, url="https://files.pythonhosted.org/packages/e7/47/d340079a2883f3850d5a9f8c478852eb2a44e8b3e50fc8e8fd40e2e84532/scikit_posthocs-0.3.6-py2.py3-none-any.whl")
	version("0.3.7", sha256="47ede89ddc6772d160ca3b88de10fa1ff8da440b2e06da0605e278429badf259", expand=False, url="https://files.pythonhosted.org/packages/e9/3e/66d9fb57aba8bd439193610fb510e363f45258905893bfd93f633afdf7dc/scikit_posthocs-0.3.7-py2.py3-none-any.whl")
	version("0.3.8", sha256="7f242d0a706f7832a715335a9dd8dc429abd27b5590f3bffcdacc6be8063f81a", expand=False, url="https://files.pythonhosted.org/packages/5d/e6/63a3265c772a0f22dba5fb1d770266bb5849765ff5a00bdf54ddf3e1969a/scikit_posthocs-0.3.8-py2.py3-none-any.whl")
	version("0.3.9", sha256="67cb2fc473946f79a22210c2d2079a8dd62f5e6d79bd1f1dbd1f773d4849163a", expand=False, url="https://files.pythonhosted.org/packages/b7/cd/053ba2fa7bdc1c79c63c6d048205cececf1dfe10b326c2109fc2eb222f45/scikit_posthocs-0.3.9-py2.py3-none-any.whl")
	version("0.4.0-py3.7", sha256="1beb556bdde4f90248fa95ef64ddca63fbcae34ab2092727b6992bebff851c8f", expand=False, url="https://files.pythonhosted.org/packages/e4/1a/da7d7c437680cc266fcdbb9b827445a3f2c30dd0f9986f8f6091f24516b9/scikit_posthocs-0.4.0-py2.py3-none-any.whl")
	version("0.5.0", sha256="7a48124794872e98b60dfdf6a6271abfd8b5abf4c0f9660e62eb48d97264fe1c", expand=False, url="https://files.pythonhosted.org/packages/1a/e3/d9ea6a17fd62b32aa37444eeeaf61de584e25768d3a811a9977b30a50735/scikit_posthocs-0.5.0-py2.py3-none-any.whl")
	version("0.5.1", sha256="d9d75675ad38de29e474f3e55980c2e6b1196548fc9e84e333d809bd418bae4d", expand=False, url="https://files.pythonhosted.org/packages/3c/ae/b25507e50507e23c27f6a54f16ca335e354846a02b3430617bb0bdbe5d3f/scikit_posthocs-0.5.1-py2.py3-none-any.whl")
	version("0.5.2", sha256="8174d347b43b6c7c17f9b9779623c6d1293edabef2385825272c93b0888161f8", expand=False, url="https://files.pythonhosted.org/packages/90/58/c001e8decf7315db869cea255c7d1e183366651bf5ac8694f3a75605fa24/scikit_posthocs-0.5.2-py2.py3-none-any.whl")
	version("0.5.3", sha256="e33437b1146b915a6cd9b74e27f657fda5405d91c83be36039bd3f5e01587be6", expand=False, url="https://files.pythonhosted.org/packages/3f/f3/005c9b14db3967a857d92ee9912ad09ea2036c08d4b4a63891eaa1fe75b8/scikit_posthocs-0.5.3-py2.py3-none-any.whl")
	version("0.5.4", sha256="eeabedddb99ebaf277a7a4f70c4a469e73512d589192194b4556bcbd4f224857", expand=False, url="https://files.pythonhosted.org/packages/71/48/7e1b401efe4c25f7428bc9be5cd9f2fa709045f6625e9a304e6283bb904a/scikit_posthocs-0.5.4-py2.py3-none-any.whl")
	version("0.6.0", sha256="2452b098d7a6bf2ab9c0a130359336424ebeb158335d13be57988ea44c8c8b1e", expand=False, url="https://files.pythonhosted.org/packages/0e/9b/96cd83dba7b60fe439de534fb71b6218574a5b41ca78eb0083dc29711758/scikit_posthocs-0.6.0-py2.py3-none-any.whl")
	version("0.6.1", sha256="cac7e92c42519ddb65ad99605d0b1c4bb7e29579ca6cb5f85b2e5c18d6c7767f", expand=False, url="https://files.pythonhosted.org/packages/ef/df/e0b951218859b06b61e0efcd26728c4df774b90e4ff204cfb1f27f575603/scikit_posthocs-0.6.1-py2.py3-none-any.whl")
	version("0.6.2", sha256="ab4e947241b3a7850bf4d89f52a80b6b83668c071c4b93e4d254d28fd2ddbe23", expand=False, url="https://files.pythonhosted.org/packages/16/a2/a7b3ef9e44e070e001ef910ae20db079c3910719301b9597e5805e469dbd/scikit_posthocs-0.6.2-py3-none-any.whl")
	version("0.6.3", sha256="ffefd54a54b276a7962d989b937d99f47f2f8fd24ad05d0fcbd088a9f0ba0eba", expand=False, url="https://files.pythonhosted.org/packages/ac/b8/ffaa42e40143825b4ae618a5b96196a934fb5f41229fc3235f35dd81a29c/scikit_posthocs-0.6.3-py3-none-any.whl")
	version("0.6.4", sha256="3923e6bf6726e27eca488cbf46dcef2e5850f9fd89524f7ceb45701c9a44697e", expand=False, url="https://files.pythonhosted.org/packages/3b/b8/8a9769c7a286070f74fbc56bcede507680210010ce0887c70112e70ced5a/scikit_posthocs-0.6.4-py3-none-any.whl")
	version("0.6.5", sha256="a5f58f0b390daac33e909ade3b736ebfa614b60cb7fa2afd5ad68d9d02e5df5e", expand=False, url="https://files.pythonhosted.org/packages/51/3f/d91af38434dfd4724959cc177350fa57acd3c0f834fcb9f96ea3b62078b0/scikit_posthocs-0.6.5-py3-none-any.whl")
	version("0.6.6", sha256="7b5078875c2774fcf0617ddd5b13c1631b82707bde243788b906aeea2bd657cb", expand=False, url="https://files.pythonhosted.org/packages/e8/b3/ab9b240381d6218a3a5e94d11a1552217317d9624988cf279ec527b5f83e/scikit_posthocs-0.6.6-py3-none-any.whl")
	version("0.6.7", sha256="8365e2525473438f769e2417c702a884b2d02079723645f25be0cdbdd9fd47b5")
	version("0.7.0", sha256="63e83432202c7fbd28fb2180ac23202c2572696f46451efe782f011ed854f945", expand=False, url="https://files.pythonhosted.org/packages/56/56/b70231055b25e298799410b78e8de1a769d64c1468913bb5282632373ed0/scikit_posthocs-0.7.0-py3-none-any.whl")
	version("0.8.0", sha256="21bf2abb6228e99e5428ca3625d4948518b1f09b447dcf5db112e3d16d6957b0", expand=False, url="https://files.pythonhosted.org/packages/c5/fe/166161978e728e7a0aeb62651aa1921b30fb7da1f056e18604dab79e99fe/scikit_posthocs-0.8.0-py3-none-any.whl")
	version("0.8.1", sha256="c3dcf59a5f1bdc316e42c71a8a8c4424c853ce841762756a3080ab4ac789b6e0", expand=False, url="https://files.pythonhosted.org/packages/43/bd/ca9d53c0e5abd1ef3c3717a4a9070e3ee339116b82c0c6cd28df51a921c6/scikit_posthocs-0.8.1-py3-none-any.whl")
	version("0.9.0", sha256="86772d3b049b9879569446f134b00410ca7d2607ffc7ea940bbc869a7a3c3410", expand=False, url="https://files.pythonhosted.org/packages/7e/8f/a4d9542ea371be2a71abd4100e646cfc957d20871c4bc571b5f1d5d662c1/scikit_posthocs-0.9.0-py3-none-any.whl")
	version("0.9.1", sha256="b071e8adf07be67b81aaba61e779e5470b07598fff1df1c25bec9aa9843beb13", expand=False, url="https://files.pythonhosted.org/packages/23/28/2417acbd5a91285e47e5b355d94aa112740f70b4ac8a7f3219db4c0c4ec6/scikit_posthocs-0.9.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-statsmodels", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("python@3.7", when="@0.4.0-py3.7", type=("build", "run"))

# {'numpy': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.3.4', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0-py3.7', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.8.0', '0.8.1', '0.9.0', '0.9.1'], 'scipy>=1.9.0': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.9.0', '0.9.1'], 'statsmodels': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.3.4', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0-py3.7', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.8.0', '0.8.1', '0.9.0', '0.9.1'], 'pandas>=0.20.0': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.8.0', '0.8.1', '0.9.0', '0.9.1'], 'seaborn': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.3.4', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0-py3.7', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.8.0', '0.8.1', '0.9.0', '0.9.1'], 'matplotlib': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.3.4', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0-py3.7', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.8.0', '0.8.1', '0.9.0', '0.9.1'], 'pytest;extra=="test"': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.9.1'], 'coverage;extra=="test"': ['0.10.0', '0.11.0', '0.11.1', '0.11.2', '0.11.3', '0.11.4', '0.9.1'], 'scipy': ['0.3.4', '0.3.6', '0.3.7', '0.3.8', '0.3.9', '0.4.0-py3.7', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0', '0.8.0', '0.8.1'], 'pandas': ['0.3.4', '0.3.6', '0.3.7'], 'pandas(>=0.20.0)': ['0.3.8', '0.3.9', '0.4.0-py3.7', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.5.4', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.5', '0.6.6', '0.7.0'], "pytest;extra=='test'": ['0.8.0', '0.8.1', '0.9.0'], "coverage;extra=='test'": ['0.8.0', '0.8.1', '0.9.0']}