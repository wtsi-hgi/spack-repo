# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBiothingsClient(PythonPackage):
	"""Python Client for BioThings API services."""
	
	homepage = "https://github.com/biothings/biothings_client.py"
	pypi = "biothings-client/biothings_client-0.4.1-py3-none-any.whl" 

	version("0.1.0", sha256="afd5a49164ce44e4d10e74c51cb77141768f7d4bf39f501ffe9ea7d548c98c9c", expand=False, url="https://files.pythonhosted.org/packages/ce/79/e2ddec944ce787bf80503f672632e5dbb3a9e1fd41608ab6304608b48511/biothings_client-0.1.0-py2.py3-none-any.whl")
	version("0.1.1", sha256="c32ba9f964ab703d5a13d8b436f7750a3df24969689a1b09a18680775974aeba", expand=False, url="https://files.pythonhosted.org/packages/79/fa/ae3b64076d18400ee933cf1c16064ea55d3cccc0bff7059695219a569f62/biothings_client-0.1.1-py2.py3-none-any.whl")
	version("0.2.0", sha256="b245dea87608ce6c4007285dadaa69f713fc4549277da5e98a8a3e73139c234a", expand=False, url="https://files.pythonhosted.org/packages/c3/ab/3930be24a748951d21ab639e60ad9dc6ff483b7e0acc5e399172d2df5f9a/biothings_client-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="8dca389165cfa2c924d6544a16c695d3e5c709f9e01607198dae29fe684ff84f", expand=False, url="https://files.pythonhosted.org/packages/b9/fd/4954f8ef8db9a9e3fc56cf96d5c132cd85ef483c4d41710a2586798d9d99/biothings_client-0.2.1-py2.py3-none-any.whl")
	version("0.2.2", sha256="40425a8333687951f90b34d79163442fb503439c75ba08b001a9ed95554b78d3", expand=False, url="https://files.pythonhosted.org/packages/0e/54/8a4984af0b29d4cc561f7fbeac68f49868c78cff897d244568438d377df5/biothings_client-0.2.2-py2.py3-none-any.whl")
	version("0.2.3", sha256="07cebb8ac199819152fdf34e41ee0b23748a937041e24756c870cadd07e3f307", expand=False, url="https://files.pythonhosted.org/packages/fb/fb/801e343910f76662d9201cde2eaad1cb1f2d5d9a8f0b1dc8fc632177c6ac/biothings_client-0.2.3-py2.py3-none-any.whl")
	version("0.2.4", sha256="4f0a2da68ba2080391b752d9708fee593e2ac8698d78c76c6e840e3a26da7390", expand=False, url="https://files.pythonhosted.org/packages/08/b7/ae5c11c62833aa21d3ef7369d2e2cc58ff56d62dba3815c9e51ac1c3ced5/biothings_client-0.2.4-py2.py3-none-any.whl")
	version("0.2.5", sha256="dee9ed5fd11a810280115eef44a81cec645c0f7cbd6b8f1aa8b205c2c0f36428", expand=False, url="https://files.pythonhosted.org/packages/de/be/9d8a5f5fee090c4da05a4277bb5f6f311cab38b05c7d61af19eaeb34469f/biothings_client-0.2.5-py2.py3-none-any.whl")
	version("0.2.6", sha256="f88f3dfcc962d84b3555a426ae59cf4752761c17b8968ae60532109b9e8a232e", expand=False, url="https://files.pythonhosted.org/packages/67/45/595faf22215de8d56900143572747357af67b48c62513383489a41b7d31a/biothings_client-0.2.6-py2.py3-none-any.whl")
	version("0.3.0", sha256="3f80b20663874b22f01ee582fdb60cd24edfff61325ea7eca2e73311245db2e3", expand=False, url="https://files.pythonhosted.org/packages/13/2d/37f64ca3f3c2932905ca85b75d3576a62621834b7d1324b2a000f63bfa84/biothings_client-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="c08437f652d9282da785e098288ef7cf3aa2a79f5d90c480eadfce96b846013e", expand=False, url="https://files.pythonhosted.org/packages/c2/21/6c4bdb8ba8d2cdeb5ac3a6460ab1cbd841e46cd851d6b00028b327c5deb3/biothings_client-0.3.1-py2.py3-none-any.whl")
	version("0.4.0", sha256="1d1178f7cc95c6926babbd3bbddf915921fba43fbd7109a33d31d4451354c6a9", expand=False, url="https://files.pythonhosted.org/packages/e8/c4/64ddf9b11d8fa0cc3d8f95beea5679d26841e72166cc3573a9fb44ad4cf9/biothings_client-0.4.0-py3-none-any.whl")
	version("0.4.1", sha256="9cbc17461b2bf6af6ed200929b886d6670d450af2034b428cd833f725695265a", expand=False, url="https://files.pythonhosted.org/packages/dc/6d/130477cfbd7294949b919c45cc1ed14a642cec95afba06a54400a4419235/biothings_client-0.4.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-httpx", type=("build", "run"))

# {'requests(>=2.3.0)': ['0.1.0', '0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.3.0'], "requests-cache(>=0.4.13);extra=='caching'": ['0.1.0', '0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.3.0'], "pandas(>=0.18.0);extra=='dataframe'": ['0.1.0', '0.1.1', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.3.0'], "pyld(>=0.7.2);extra=='jsonld'": ['0.1.1'], 'nose': ['0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4'], "PyLD(>=0.7.2);extra=='jsonld'": ['0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.2.4', '0.2.5', '0.2.6', '0.3.0'], 'requests>=2.3.0': ['0.3.1'], "requests-cache>=0.4.13;extra=='caching'": ['0.3.1'], "pandas>=0.18.0;extra=='dataframe'": ['0.3.1'], "PyLD>=0.7.2;extra=='jsonld'": ['0.3.1'], 'httpx>=0.22.0': ['0.4.0', '0.4.1'], 'importlib-metadata;python_version<"3.8"': ['0.4.0', '0.4.1'], 'anysqlite;python_version>="3.8"andextra=="caching"': ['0.4.0', '0.4.1'], 'hishel[sqlite];python_version>="3.8"andextra=="caching"': ['0.4.0', '0.4.1'], 'pandas>=1.1.5;extra=="dataframe"': ['0.4.0', '0.4.1'], 'PyLD>=0.7.2;extra=="jsonld"': ['0.4.0', '0.4.1'], 'pytest>=7.0.1;extra=="tests"': ['0.4.0', '0.4.1'], 'pytest-asyncio>=0.16.0;extra=="tests"': ['0.4.0', '0.4.1']}