# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDepinfo(PythonPackage):
	"""List any package's direct dependencies and their versions."""
	
	homepage = "https://github.com/Midnighter/dependency-info"
	pypi = "depinfo/depinfo-2.2.0-py3-none-any.whl" 

	version("1.0.3", sha256="d6e49362494d1448c35aaeee0d815fd8d0b85d42534a2b23effeae421ee342bf", expand=False, url="https://files.pythonhosted.org/packages/b2/20/c3d7fa01bf994429f24776f4746957e0aadda5a9b75303784e788b0aba97/depinfo-1.0.3-py2.py3-none-any.whl")
	version("1.1.0", sha256="0ab80d7b57a6931ba36d9ec0c8ff3528ea2a565e8f13069d6299aa75341ef075", expand=False, url="https://files.pythonhosted.org/packages/8d/1e/07781f93079129ca99503094c27f4a9f2470560f9a5cffd6806cd2d8d6f3/depinfo-1.1.0-py2.py3-none-any.whl")
	version("1.2.0", sha256="a9b878f939bd8af7c2d11ac89c5192e3765e56c4a66c741fe7d9a24d51ed7ff1", expand=False, url="https://files.pythonhosted.org/packages/15/4a/c67b5d8efc8893133b842a8a113d12e3a670ad73cc4203f2cfe251c40864/depinfo-1.2.0-py2.py3-none-any.whl")
	version("1.3.0", sha256="a9dc0f3e73658f72b41ac9b87c2e05fc887d64f74b0799381dd5c872be83de59", expand=False, url="https://files.pythonhosted.org/packages/23/75/97ffbbaa7dba4ff40988d6c03b20f489c075cd814af18382a907ff622fbe/depinfo-1.3.0-py2.py3-none-any.whl")
	version("1.4.0", sha256="33eb3f43d82e198bb5c6164472a108a66dc969aca930ccbab4480f469af3def8", expand=False, url="https://files.pythonhosted.org/packages/25/a4/75052b758112911810860bcef154596012232e339dad122d3ff443f179b8/depinfo-1.4.0-py2.py3-none-any.whl")
	version("1.5.0", sha256="fed1cfd18bc6c504e797ae52437579f3d3cb923173de30ef3eff2b78ab1dd04a", expand=False, url="https://files.pythonhosted.org/packages/08/61/80660048813d3dc6850d6e940b72f4bc42a35a897280fd8e2aa2f9df2bfa/depinfo-1.5.0-py2.py3-none-any.whl")
	version("1.5.1", sha256="30dddb9059166e96039e9676689c2a0edd4fd4d0b0624486aab1f78dc0e68b13", expand=False, url="https://files.pythonhosted.org/packages/1d/a3/c5d91c1e91a0e3c61c19563e224bda4f22fc24b6a86ef1c7e00f66ea9c4e/depinfo-1.5.1-py2.py3-none-any.whl")
	version("1.5.3", sha256="32e1f7e17dbf4251db13c4f1fe5452539be9acaae0a2218df74bf59d7f80a909", expand=False, url="https://files.pythonhosted.org/packages/e4/52/815b70d52b495bce1558d61a5e2fa4dffc1d696e1c5c65bfdd3c04b4bc90/depinfo-1.5.3-py2.py3-none-any.whl")
	version("1.5.4", sha256="0784320bb50f3ef81f2b403213316b5343359b40c0e7eccba201b1a03f167ab8", expand=False, url="https://files.pythonhosted.org/packages/1c/40/d97672eff0338ece9cb4c31640cfcbb72c325dbb9e1fa14efba8ef81a180/depinfo-1.5.4-py2.py3-none-any.whl")
	version("1.6.0", sha256="6610b6eaa58b6914c692e606bd8b037bfade58167c1ea37e050fd4cae30db2c9", expand=False, url="https://files.pythonhosted.org/packages/d4/50/0ddb38eb8714105a707a37349efeb523c82b4553a07fd4e114df4fb88807/depinfo-1.6.0-py2.py3-none-any.whl")
	version("1.7.0", sha256="5f772fdcd5a376f2d5c01e6eac7120d91316536b1e1885aea1e87f03f86a38ab", expand=False, url="https://files.pythonhosted.org/packages/af/8b/cee6dca4c4708705444c9cad9e783b9212cc51cab8a5e05ccfe930f53058/depinfo-1.7.0-py2.py3-none-any.whl")
	version("2.0.0", sha256="7dbb2a1fa858b508ae1966a177a879d7798d155d48b8aa8ee10f7b43e3e79229", expand=False, url="https://files.pythonhosted.org/packages/71/3e/57cf811a2303834b6f56caeee303d476398de60f0118046e2c55b30c5476/depinfo-2.0.0-py3-none-any.whl")
	version("2.1.0", sha256="81b8f405713ebc9ebf5bc60ee9850a230ddb1550da09c89b531c2d5640b20ef4", expand=False, url="https://files.pythonhosted.org/packages/64/a1/432a16404700353d7ec4a65e50a294627a8ed96bfeb2150c1ce157ce5649/depinfo-2.1.0-py3-none-any.whl")
	version("2.1.1", sha256="bb0ca795e580c0c90999303196997783a0f7213db580973aa03fe14254ad88e0", expand=False, url="https://files.pythonhosted.org/packages/03/88/898bf3e5e1caab7da49ca7298a6c2f1a4189ef3f6864614fd345b3a1ea8e/depinfo-2.1.1-py3-none-any.whl")
	version("2.2.0", sha256="3d9ba933e7a9d718b9915f75c844a38c5603cd3cdba1816ab95e0b148b100d8f", expand=False, url="https://files.pythonhosted.org/packages/1f/10/5fe7a7778cc8a701373662f99393f443541353018d3cf2bf6c8f91b032d6/depinfo-2.2.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))

# {'pipdeptree(>=0.13.2)': ['1.0.3', '1.5.0', '1.5.1', '1.5.3', '1.5.4'], "black;extra=='development'": ['1.0.3', '1.5.0', '1.5.1', '1.5.3', '1.5.4', '1.6.0', '1.7.0', '2.0.0', '2.1.0', '2.1.1', '2.2.0'], "isort;extra=='development'": ['1.0.3', '1.5.0', '1.5.1', '1.5.3', '1.5.4', '1.6.0', '1.7.0', '2.0.0', '2.1.0', '2.1.1', '2.2.0'], "tox;extra=='development'": ['1.0.3', '1.5.0', '1.5.1', '1.5.3', '1.5.4', '1.6.0', '1.7.0', '2.0.0', '2.1.0', '2.1.1', '2.2.0'], 'pipdeptree': ['1.1.0', '1.2.0', '1.3.0', '1.4.0'], 'importlib-metadata;python_version<"3.8"': ['1.6.0', '1.7.0', '2.0.0', '2.1.0', '2.1.1', '2.2.0'], "rich;extra=='rich'": ['2.0.0', '2.1.0', '2.1.1', '2.2.0']}