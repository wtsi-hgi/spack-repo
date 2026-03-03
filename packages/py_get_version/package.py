# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGetVersion(PythonPackage):
	"""A version helper in the spirit of versioneer."""
	
	homepage = "https://github.com/flying-sheep/get_version"
	pypi = "get-version/get_version-3.5.5-py3-none-any.whl" 

	version("1.0.0", sha256="bdc367c866064e98b0121bac0ab2164d231531c9c445eac8cdda4406b787f167")
	version("2.0.0", sha256="b7290b990ef9868f9f184ffb7bdf67fe57e490c67ed1dc60e77d490cc3d32817", expand=False, url="https://files.pythonhosted.org/packages/dc/6b/b451ca80e76b99a19ec23fb9cbc489d3d0af76cb5d8a2ff7dcadef845de2/get_version-2.0.0-py3-none-any.whl")
	version("2.0.1", sha256="e918b5ae0a724d94f0356d498036fcb51b257848149b90b6f8b6c9358f79fcee", expand=False, url="https://files.pythonhosted.org/packages/29/49/19de8ef0548fd0eaf80e404ce6325d81bf543cc9c7441733cee1916354be/get_version-2.0.1-py3-none-any.whl")
	version("2.0.2", sha256="4c31305523d86d82690292587c4ef4007037e0296cf61d737766a7f2d22d0ecb", expand=False, url="https://files.pythonhosted.org/packages/bc/be/e84a50e88af433a07b4ff489e34057c69f3878ef8e59395567f26c2ea3da/get_version-2.0.2-py3-none-any.whl")
	version("2.0.3", sha256="4bc0e529f9678eb8188265205924499e37e22054a29036ed4ca2437ff96ab7e5", expand=False, url="https://files.pythonhosted.org/packages/05/27/5adb1ac33ffcf532d3e83cc49cafa72760d5d53756068482feefd1b67ac3/get_version-2.0.3-py3-none-any.whl")
	version("2.0.4", sha256="2405f53bbd15cc2f4f3f6548b2ac60331b6d68c5b94c95267d9286078f7c468e", expand=False, url="https://files.pythonhosted.org/packages/4d/0f/65bb6208f08298cecf94140df0b3b1a0028b4ee79ff7a961c990dccb1a98/get_version-2.0.4-py3-none-any.whl")
	version("2.0.5", sha256="429a887efe4ffecdb89324c3758dac096f987c3b87027ecc7c9a6293c19eb834", expand=False, url="https://files.pythonhosted.org/packages/a4/62/f742cc9c19bb8a5107443d289a7ed0777aabbfde61ba28aaf105df2e7765/get_version-2.0.5-py3-none-any.whl")
	version("2.0.6", sha256="437143718f704b035cb20fa44eae440618a1a2a806fa360ec5c3dc4e1094e41d", expand=False, url="https://files.pythonhosted.org/packages/2d/27/610ef458455cb1bcc4b454cebab43de3579e43d080af872727b9ac3146c8/get_version-2.0.6-py3-none-any.whl")
	version("2.1", sha256="f5481b7b00bebf4cf52daa43510ef439be51b78665c4df29ad6088fcd7203382", expand=False, url="https://files.pythonhosted.org/packages/23/48/7610e884e62fff2183e7bc8592397c39a020267fb5147905fcd3f9cc820c/get_version-2.1-py3-none-any.whl")
	version("2.2", sha256="5bfe61d334964a0d44da2e2002bd1ada50df3a5d767993b8faa6888590f5c726", expand=False, url="https://files.pythonhosted.org/packages/30/a6/97f1c2cdaae1355f79d24264d3ddbcbb6ba670f5994c5997b688d5cd10e5/get_version-2.2-py3-none-any.whl")
	version("3.0", sha256="db2f31c281c41fba93f2546539a30c8d906f3d27fe2f8d229825e4292a671c93", expand=False, url="https://files.pythonhosted.org/packages/d7/b2/e47643bb1418642070da5b60552b2042f1001aa5802dc0937f8de4997cbc/get_version-3.0-py3-none-any.whl")
	version("3.1", sha256="168f5a19709dc6e0f864495728f3807ca84f652f335e82bba6a000e4dc0c7c26", expand=False, url="https://files.pythonhosted.org/packages/31/85/b40de1adf9175695549ca9502be1c4699f42d7746b01f8a7b4594bec4efe/get_version-3.1-py3-none-any.whl")
	version("3.2", sha256="0da384db12fa61ea25067b576b47bf83d539f30e14f3e44f4fe8b59b1656b708", expand=False, url="https://files.pythonhosted.org/packages/2e/eb/4892cfbc7a3275306f41b74dd86e516041e58b67d1daa30c44861a6f0510/get_version-3.2-py3-none-any.whl")
	version("3.3", sha256="a5ce6f47e0adef0327938cb168edf11a6fb55d695b0b5a44a5085f314a183f81", expand=False, url="https://files.pythonhosted.org/packages/23/70/84e84d2ed94e03f2e0d3f378735d107c9e41d02de756b7ecf77e327c0fbb/get_version-3.3-py3-none-any.whl")
	version("3.4", sha256="ea23b470a764c6d0cde4ec540414c5b6a03b9ca2fb176f694b38bea4690a2035", expand=False, url="https://files.pythonhosted.org/packages/80/7a/7af1deca2c3df26600eae5b773ed0025b7cfd54716e5538d40483e696c85/get_version-3.4-py3-none-any.whl")
	version("3.5", sha256="8f1cd750e7d15d3b0119363ab090b39f0924523565a8a637b9134e9ec891068e", expand=False, url="https://files.pythonhosted.org/packages/84/e8/aa954bc4ab5104bf84eeece1bda1e3d1e2378c8978a1c2cd38c1adfb15f1/get_version-3.5-py3-none-any.whl")
	version("3.5.1", sha256="ef059649fc985c9317805975031aced6eadd7f8f3316813bbf1fed6b0d3dbadc", expand=False, url="https://files.pythonhosted.org/packages/9b/6a/c0e0c7d25e74a621afd61429510314c2df795ec212c787cd4709bd09bbf1/get_version-3.5.1-py3-none-any.whl")
	version("3.5.2", sha256="08584badece1704b250aefaf0bff1b383631154f8bd14c2fcb10595db1ebe8c5", expand=False, url="https://files.pythonhosted.org/packages/2f/b8/78ce4ca8cfba31ba95cb56b1c7a329687bd45fdb8f7c4615c9f05b7c7313/get_version-3.5.2-py3-none-any.whl")
	version("3.5.3", sha256="7a6903db2da84fa3b38a0185bed7ea55a804a087a846680edc1a5df66dce0491", expand=False, url="https://files.pythonhosted.org/packages/47/bb/c231518678571c656a2f5e958ed1c0f7cd870518471631b661675e1806c6/get_version-3.5.3-py3-none-any.whl")
	version("3.5.4", sha256="d49d9d897116ffcc1fac7773dea00d9de44ca1905b83955f3309bcd281cf063a", expand=False, url="https://files.pythonhosted.org/packages/f9/1a/120c6885a7b31d6fbd29751543bd794eb6d6a854ab7f8293302a51f09998/get_version-3.5.4-py3-none-any.whl")
	version("3.5.5", sha256="a0748c95e846692a26f6ffb5858153c302519cc09e3c7397f7595f8d2a0d9997", expand=False, url="https://files.pythonhosted.org/packages/4a/19/bdf88598c77c5e6486ae4d0f6aa0877138ef6e267bfab0710a659075a2b2/get_version-3.5.5-py3-none-any.whl")

	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-dunamai", type=("build", "run"))

# {'setuptools': ['2.0.5', '2.0.6', '2.1', '2.2'], 'future-fstrings': ['2.0.5', '2.0.6'], 'pytest;extra=="test"': ['2.0.5', '2.0.6', '2.1', '2.2', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5'], 'pytest-cov;extra=="test"': ['2.0.5', '2.0.6', '2.1', '2.2', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.5.2'], 'testpath;extra=="test"': ['2.0.5', '2.0.6', '2.1', '2.2'], 'pytest-black;extra=="test"and(python_version!="3.5")': ['2.1', '2.2', '3.0', '3.1', '3.2'], 'pygments;extra=="test"': ['2.1', '2.2', '3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.5.2', '3.5.3', '3.5.4', '3.5.5'], 'dunamai': ['3.0', '3.1', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.5.2', '3.5.3', '3.5.4'], 'importlib_metadata;python_version<"3.8"': ['3.3', '3.4', '3.5', '3.5.1', '3.5.2', '3.5.3', '3.5.4'], 'pytest-black;extra=="test"': ['3.3', '3.4', '3.5', '3.5.1', '3.5.2', '3.5.3', '3.5.4', '3.5.5'], 'pytest>=6.2.5;extra=="test"': ['3.5.1', '3.5.2', '3.5.3', '3.5.4', '3.5.5'], 'pytest-mypy;extra=="test"': ['3.5.1', '3.5.2', '3.5.3', '3.5.4', '3.5.5'], 'typing_extensions;python_version<"3.8"': ['3.5.4'], 'dunamai>=1.19.0': ['3.5.5']}