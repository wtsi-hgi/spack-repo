# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyServiceIdentity(PythonPackage):
	"""Service identity verification for pyOpenSSL & cryptography."""
	
	homepage = "https://service-identity.readthedocs.io/"
	pypi = "service-identity/service_identity-24.2.0-py3-none-any.whl" 

	version("0.1-py2.7", sha256="2f98469a82851990aa8ee66cb596545fe7d6d4e5a80f63d4447a4e16ce8249c6", expand=False, url="https://files.pythonhosted.org/packages/a7/3a/389d3ac0b4a4d66ba1c4e1cb11612012dae176aa55c35db90f75a28e5ea7/service_identity-0.1-py2.py3-none-any.whl")
	version("0.2-py2.7", sha256="f3a288ddb23448e8c6498af3d7a1f1348569b3a18a4c3e645c72e180692523d1", expand=False, url="https://files.pythonhosted.org/packages/4c/0a/0e7f5420f90d99846163a1ffa9a6b1be29fffbaf7e6d3827cda4293f53ae/service_identity-0.2-py2.py3-none-any.whl")
	version("1.0.0-py2.7", sha256="470eae43c69ec8cd1df90b0910af166f61670cebd0708c1692f19a1c14871484", expand=False, url="https://files.pythonhosted.org/packages/29/8f/9499084ea8b5db68f9211d7d772e6ba2f0576c7c422f6b67dc3881fee726/service_identity-1.0.0-py2.py3-none-any.whl")
	version("14.0.0-py2.7", sha256="c4e09794c54229a4d2bf6a784130880259f0b0870d2f40e9712dc4114f06795c", expand=False, url="https://files.pythonhosted.org/packages/98/1a/2bd789e1623a18a2e54ff57934d169e5f1599d2a719954ad67bbb8cb0f72/service_identity-14.0.0-py2.py3-none-any.whl")
	version("16.0.0", sha256="5c63e1532135f7171cb33e8b2f31c758c3ce0654e6eb198573e23d01128678d4", expand=False, url="https://files.pythonhosted.org/packages/80/f5/8b1604e4d85ce60333a2fd4bc7b7743b21949b434b7c1c2c77eee9e7cd6f/service_identity-16.0.0-py2.py3-none-any.whl")
	version("17.0.0", sha256="0e76f3c042cc0f5c7e6da002cf646f59dc4023962d1d1166343ce53bdad39e17", expand=False, url="https://files.pythonhosted.org/packages/29/fa/995e364220979e577e7ca232440961db0bf996b6edaf586a7d1bd14d81f1/service_identity-17.0.0-py2.py3-none-any.whl")
	version("18.1.0", sha256="001c0707759cb3de7e49c078a7c0c9cd12594161d3bf06b9c254fdcb1a60dc36", expand=False, url="https://files.pythonhosted.org/packages/e9/7c/2195b890023e098f9618d43ebc337d83c8b38d414326685339eb024db2f6/service_identity-18.1.0-py2.py3-none-any.whl")
	version("21.1.0", sha256="f0b0caac3d40627c3c04d7a51b6e06721857a0e10a8775f2d1d7e72901b3a7db", expand=False, url="https://files.pythonhosted.org/packages/93/5a/5e93f280ec7be676b5a57f305350f439d31ced168bca04e6ffa64b575664/service_identity-21.1.0-py2.py3-none-any.whl")
	version("23.1.0", sha256="87415a691d52fcad954a500cb81f424d0273f8e7e3ee7d766128f4575080f383", expand=False, url="https://files.pythonhosted.org/packages/0c/42/bf07f277b45da6e350df3314804aa2b5411e0938d3b78b4f17da2e1302c2/service_identity-23.1.0-py3-none-any.whl")
	version("24.1.0", sha256="a28caf8130c8a5c1c7a6f5293faaf239bbfb7751e4862436920ee6f2616f568a", expand=False, url="https://files.pythonhosted.org/packages/3b/92/44669afe6354a7bed9968013862118c401690d8b5a805bab75ac1764845f/service_identity-24.1.0-py3-none-any.whl")
	version("24.2.0", sha256="6b047fbd8a84fd0bb0d55ebce4031e400562b9196e1e0d3e0fe2b8a59f6d4a85", expand=False, url="https://files.pythonhosted.org/packages/08/2c/ca6dd598b384bc1ce581e24aaae0f2bed4ccac57749d5c3befbb5e742081/service_identity-24.2.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-attrs", type=("build", "run"))
	depends_on("py-cryptography", type=("build", "run"))
	depends_on("py-pyasn1", type=("build", "run"))
	depends_on("py-pyasn1-modules", type=("build", "run"))
	depends_on("python@2..7", when="@0.1-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.2-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@1.0.0-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@14.0.0-py2.7", type=("build", "run"))

# {'pyasn1': ['0.1-py2.7', '0.2-py2.7', '1.0.0-py2.7', '14.0.0-py2.7', '16.0.0', '17.0.0', '18.1.0', '21.1.0', '23.1.0', '24.1.0', '24.2.0'], 'pyasn1-modules': ['0.1-py2.7', '0.2-py2.7', '1.0.0-py2.7', '14.0.0-py2.7', '16.0.0', '17.0.0', '18.1.0', '21.1.0', '23.1.0', '24.1.0', '24.2.0'], 'pyopenssl(>=0.12)': ['0.1-py2.7', '0.2-py2.7', '1.0.0-py2.7', '14.0.0-py2.7', '16.0.0', '17.0.0'], 'characteristic': ['1.0.0-py2.7'], 'characteristic(>=14.0.0)': ['14.0.0-py2.7'], 'attrs': ['16.0.0', '17.0.0'], "idna;extra=='idna'": ['16.0.0', '17.0.0', '18.1.0', '21.1.0', '23.1.0', '24.1.0', '24.2.0'], 'attrs(>=16.0.0)': ['18.1.0'], 'cryptography': ['18.1.0', '21.1.0', '23.1.0', '24.1.0', '24.2.0'], 'ipaddress;python_version<"3.3"': ['18.1.0', '21.1.0'], "coverage(>=4.2.0);extra=='dev'": ['18.1.0'], "pytest;extra=='dev'": ['18.1.0', '21.1.0', '24.2.0'], "sphinx;extra=='dev'": ['18.1.0', '21.1.0'], "idna;extra=='dev'": ['18.1.0', '21.1.0', '24.2.0'], "pyOpenSSL;extra=='dev'": ['18.1.0', '21.1.0'], "sphinx;extra=='docs'": ['18.1.0', '21.1.0', '23.1.0', '24.1.0', '24.2.0'], "coverage(>=4.2.0);extra=='tests'": ['18.1.0'], "pytest;extra=='tests'": ['18.1.0', '21.1.0', '23.1.0', '24.1.0', '24.2.0'], 'attrs(>=19.1.0)': ['21.1.0'], 'six': ['21.1.0'], "coverage[toml](>=5.0.2);extra=='dev'": ['21.1.0'], "furo;extra=='dev'": ['21.1.0'], "furo;extra=='docs'": ['21.1.0', '23.1.0', '24.1.0', '24.2.0'], "coverage[toml](>=5.0.2);extra=='tests'": ['21.1.0'], 'attrs>=19.1.0': ['23.1.0', '24.1.0', '24.2.0'], "pyopenssl;extra=='dev'": ['23.1.0', '24.1.0', '24.2.0'], "service-identity[docs,idna,mypy,tests];extra=='dev'": ['23.1.0'], "myst-parser;extra=='docs'": ['23.1.0', '24.1.0', '24.2.0'], "pyopenssl;extra=='docs'": ['23.1.0', '24.1.0', '24.2.0'], "sphinx-notfound-page;extra=='docs'": ['23.1.0', '24.1.0', '24.2.0'], "idna;extra=='mypy'": ['23.1.0', '24.1.0', '24.2.0'], "mypy;extra=='mypy'": ['23.1.0', '24.1.0', '24.2.0'], "types-pyopenssl;extra=='mypy'": ['23.1.0', '24.1.0', '24.2.0'], "coverage[toml]>=5.0.2;extra=='tests'": ['23.1.0', '24.1.0', '24.2.0'], "service-identity[idna,mypy,tests];extra=='dev'": ['24.1.0'], "coverage[toml]>=5.0.2;extra=='dev'": ['24.2.0'], "mypy;extra=='dev'": ['24.2.0'], "types-pyopenssl;extra=='dev'": ['24.2.0']}