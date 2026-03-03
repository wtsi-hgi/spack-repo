# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAutoflake(PythonPackage):
	"""Removes unused imports and unused variables"""
	
	homepage = "https://www.github.com/PyCQA/autoflake"
	pypi = "autoflake/autoflake-2.3.1-py3-none-any.whl" 

	version("0.0.1", sha256="1a11d63b088281b02e57872f0e02d7581d9cec2e19488cd0d2136ab6d2404cc8")
	version("0.1", sha256="92ac99c14c8cc20fc10a2804c59ccae4710e40911c2b726a52693afd3adb9311")
	version("0.1.1", sha256="2ff3e0824d071311e1abb0b05387c2b2c6bab82b57ca15d92f2b98d3345a4f07")
	version("0.1.2", sha256="7d9d07a88e998f17e4cf7ff857a767a9684818cae96452c3008a9d9721376ba6")
	version("0.1.3", sha256="59a5d6f5cdc1be1c2e1c181edde4b57d895f9b6e8860161658a5842c4a7fcde2")
	version("0.1.4", sha256="57798944d8e199f6897787dabd764aa369e59cbd9b1c95dc8a5917db2264157e")
	version("0.1.5", sha256="2b161de1126140da11802301b0d86fee01a6eeeea052c12d4cdc3b15b7fab03d")
	version("0.1.6", sha256="7d4253391fbc32a541b1844ba0eee8ef86ee87256c50d1b04cb455497fb07e66")
	version("0.1.7", sha256="04f4979d6e1ff5346e3b11db56ee259462da441a1bb22a7dbe312af0a313db07")
	version("0.2", sha256="9da6cf3f1b809f7a9027424354f7d6c7fab7f66e326d43c8b624035c9e430e1e")
	version("0.2.1", sha256="ea94d14f295a7992243c5bf59f73933767af676c960fb40e7ec127055c47b329")
	version("0.2.2", sha256="cc309f6939c168b7d128df34abd477c9e7365646f5791a85218d1277c9bf3818")
	version("0.2.3", sha256="dfdefbe980564c51ee8eeeb57b8661c5fc22ca330cc0c8756923b8e3df6d4daa")
	version("0.3", sha256="4e5e98e7d1e1440a69f5066c2637ea79f984b30f5164d22f0e262b52c87eed0e")
	version("0.3.1", sha256="d86bbce7e614f87f792b08662b44ab878eda6be81d74fb847874d628d99a5239")
	version("0.3.2", sha256="afd4a2e39997aa3bcddaf84d342a78c86eef5d580285bd354f82b7ad9785dd96")
	version("0.3.3", sha256="079e947ec26a4171d46c3b42ff3febd89678b91cb2b257e5468705afaf90d558")
	version("0.4", sha256="f8b5b7d2293097aab8f84c7ed8f77506ab9ee626829751939cddf253c34ae35a")
	version("0.4.1", sha256="b0196a5766349ed76be3ef94f8381606ec39e51fae7ae9b2fdb6c87d359e2ea7")
	version("0.4.2", sha256="fb70049415de03cda515020d19cd7982185c0f9c376c4755ddf63c1079b662a9")
	version("0.4.3", sha256="9c9e48f85f68467291e9c15adcdc7a6c90051dacb666a741193758b0bd26720a")
	version("0.4.4", sha256="98635c83a85e0582b024209043ca7ea3ae6f9f043dd9292ed763764004a8d574")
	version("0.5", sha256="46cfcf55031b712fd317e734a4039bb57d7453fcdd40bc5588605aa3870c57c8")
	version("0.6", sha256="1b54327551abb9ae08cf3502e9255a555bd7a0b773453b6616fa59f4562ee874")
	version("0.6.1", sha256="af30bdaa1c5d7e68bd195b4baf42a9cd2c9d4f8ec3637dc4b36f22c11be2dfdc")
	version("0.6.2", sha256="7c9dcf74632a6f2f11cd83394e3ca4bd2f66f804b5c6fff96c2ec29561821d08")
	version("0.6.3", sha256="b918faeed1c3586967785f8287acf9606cd9ac281795f5634ca016c1ea0365d6")
	version("0.6.4", sha256="5be588d03336deb14760a9256b45e2d9d217bebbe1ade01ef3176ce2f59caac6")
	version("0.6.5", sha256="7c6d92fa1e87d1aaf6ce47fab0c290fb39b08f30b99e842f431cfcaec66f1aff")
	version("0.6.6", sha256="67f3886b74f8614b9696ea47eb9ce90fa808da142619e8e6da6eaf541df30e0f")
	version("0.7", sha256="3f3f06c4ef9f9a46961fcb0df8cd96de82208f2af96b4e75d2b419d4e6287442")
	version("1.0", sha256="0a6db5672fb8aec7414dec44b536634362b9188fc01f71e44017737538da648a")
	version("1.1", sha256="a74d684a7a02654f74582addc24a3016c06809316cc140457a4fe93a1e6ed131")
	version("1.2", sha256="c103e63466f11db3617167a2c68ff6a0cda35b940222920631c6eeec6b67e807")
	version("1.3", sha256="6b59e5b9b82e30077499578856282debb81186d10b4f899e8c2e1d616cdef973")
	version("1.3.1", sha256="680cb9dade101ed647488238ccb8b8bfb4369b53d58ba2c8cdf7d5d54e01f95b")
	version("1.4", sha256="61a353012cff6ab94ca062823d1fb2f692c4acda51c76ff83a8d77915fba51ea")
	version("1.5.0", sha256="fef6081b5e1ffc1e6aaf706c26f1f11f36df0346d4c7c21dc57e92603e493232", expand=False, url="https://files.pythonhosted.org/packages/b9/b0/190c067d30a30c8ad75dd0e99f98708d3c779eca87a263866122a43520d7/autoflake-1.5.0-py2.py3-none-any.whl")
	version("1.5.1", sha256="275e05e3caa8307269ad4d46f2e058b76a5c41ca7d1a7f57158d64e9df3ffdd6", expand=False, url="https://files.pythonhosted.org/packages/8d/32/15e43f9f6be2c8317791cdb422fe2d4ff8732b373a430f003f20562e2a89/autoflake-1.5.1-py2.py3-none-any.whl")
	version("1.5.2", sha256="3a57716fdaa6c21273b901e62a8d1682b266a2ad43f7a64e5f16663c9cdfd73c", expand=False, url="https://files.pythonhosted.org/packages/10/a6/88640bd08c778c9ff7129eda3467f69ab61152418e21f544f75e95233017/autoflake-1.5.2-py2.py3-none-any.whl")
	version("1.5.3", sha256="90eb8d3f625bd72068eb670338ea7efcddbc5c6e822d3601e3dc9404c06ea8da", expand=False, url="https://files.pythonhosted.org/packages/66/98/bb42504d2639ac9c440e695c9d8d3d5b4855ae5568090cf03e3b703ab6d9/autoflake-1.5.3-py2.py3-none-any.whl")
	version("1.6.0", sha256="d5de7da3786809bbdedbdbdeecbb410d55277b3492a4a3ede882998f1e87f156", expand=False, url="https://files.pythonhosted.org/packages/d8/bc/c9fba43a171688974618b3b9d699de2d9226a787ab260d9c9f4b12ffeb75/autoflake-1.6.0-py2.py3-none-any.whl")
	version("1.6.1", sha256="dfef4c851fb07e6111f9115d3e7c8c52d8564cbf71c12ade2d8b8a2a7b8bd176", expand=False, url="https://files.pythonhosted.org/packages/14/31/bb02ec9fd27b688dfa966c1bd71b21337c1765aec7d69376657757173369/autoflake-1.6.1-py2.py3-none-any.whl")
	version("1.7.0", sha256="cb46baf67d7114302cf66363f384d34704508828f1606a42a267957531f2bab3", expand=False, url="https://files.pythonhosted.org/packages/97/88/4fd91d53b6d4c6a918a0aab5b81d982d65d56b0f7775472fe6f78d148e03/autoflake-1.7.0-py2.py3-none-any.whl")
	version("1.7.1", sha256="b759b1aee50526cc169a812a9a0de49b808c3de6be7166690e93bb36a7f23c98", expand=False, url="https://files.pythonhosted.org/packages/d6/fd/3ba52cb635c38f6749a5c07867ac5e1a9fd9e1675b82e6fa6e245a70c733/autoflake-1.7.1-py2.py3-none-any.whl")
	version("1.7.3", sha256="f465256141901a364fa60578d6c6d87414316ea9a79f0994792f32cdb044ca9e", expand=False, url="https://files.pythonhosted.org/packages/d7/df/ac7318934698dc44fd56b814e1c869b54b4ee47b9db6ea330c37c2050f0a/autoflake-1.7.3-py2.py3-none-any.whl")
	version("1.7.4", sha256="9daac24b55cb0eed619e8260c4c15e6572b7a28e8f55c8ac23530766d7f4c957", expand=False, url="https://files.pythonhosted.org/packages/33/f2/e7cacd78fe7d0c6466017281563a63878ed6c035c956bed7c92d9f29f052/autoflake-1.7.4-py2.py3-none-any.whl")
	version("1.7.5", sha256="bedb29201b07876cd9cad3a804760b1127b9bf156cf9689762a12eabd1683b65", expand=False, url="https://files.pythonhosted.org/packages/f5/fb/466dcc38f159343df1d4e7ef67c0a3a9c2dfa83e58d646ff70167e04ee9a/autoflake-1.7.5-py2.py3-none-any.whl")
	version("1.7.5", sha256="5ce7977d4f9905b01ef12d572f69252406009718ec1bac95fb5d74eb4faca58b", expand=False, url="https://files.pythonhosted.org/packages/24/a9/642d91a1f0a577159dbe7bc82e1440513b13d6002ed21e9c1df28a8b3e6d/autoflake-1.7.5-py3-none-any.whl")
	version("1.7.6", sha256="9fa63cb814c1dfc02103a361b449c024226348c2130b6839cd94278c309c4a65", expand=False, url="https://files.pythonhosted.org/packages/4a/71/58bd9c30b2e3ad15b063e61cbc52929aa39c1ca5106f887ff7251f323bfa/autoflake-1.7.6-py3-none-any.whl")
	version("1.7.7", sha256="a9b43d08f8e455824e4f7b3f078399f59ba538ba53872f466c09e55c827773ef", expand=False, url="https://files.pythonhosted.org/packages/da/7d/6cfefbc9db987d211526a62ea79a8bdc3fdde0e0c04282bc6db07be5fc58/autoflake-1.7.7-py3-none-any.whl")
	version("1.7.8", sha256="46373ef69b6714f5064c923bb28bd797c4f8a9497f557d87fc36665c6d956b39", expand=False, url="https://files.pythonhosted.org/packages/64/fb/e2dc6e8f7e6ee4202581a9c8e4f5b9531e9b395b949d96a1956b43820925/autoflake-1.7.8-py3-none-any.whl")
	version("2.0.0", sha256="d58ed4187c6b4f623a942b9a90c43ff84bf6a266f3682f407b42ca52073c9678", expand=False, url="https://files.pythonhosted.org/packages/48/ec/a2761b7f2cb825f1e4e9073858c8111ac8c74fc0e945456a964e17353c1f/autoflake-2.0.0-py3-none-any.whl")
	version("2.0.1", sha256="143b0843667734af53532c443e950c787316b9b1155b2273558260b44836e8e4", expand=False, url="https://files.pythonhosted.org/packages/7b/68/13f71734e97fb6fc24baf2ec9e4971ead3a3d54bfc1a44f143ce6a2b53e8/autoflake-2.0.1-py3-none-any.whl")
	version("2.0.2", sha256="a82d8efdcbbb7129a8a23238c529fb9d9919c562e26bb7963ea6890fbfff7d02", expand=False, url="https://files.pythonhosted.org/packages/34/47/702047c981cb6376d08bdedfd99341ab418697a0145366b02007292680d8/autoflake-2.0.2-py3-none-any.whl")
	version("2.1.0", sha256="bc15c8a2e5f259d07667ea7896643494f8422ff4cd9f8393c5d12b08fa7f2fc4", expand=False, url="https://files.pythonhosted.org/packages/31/66/92259d928d0e5aa8cb1da9fd5f56f792565bac3a8f9a8967dc85ec2fcbbe/autoflake-2.1.0-py3-none-any.whl")
	version("2.1.1", sha256="94e330a2bcf5ac01384fb2bf98bea60c6383eaa59ea62be486e376622deba985", expand=False, url="https://files.pythonhosted.org/packages/50/4c/24cf18273b0a76cd31255b76f76999dbbeba119c3dd370a6ed84b0f1e85f/autoflake-2.1.1-py3-none-any.whl")
	version("2.2.0", sha256="de409b009a34c1c2a7cc2aae84c4c05047f9773594317c6a6968bd497600d4a0", expand=False, url="https://files.pythonhosted.org/packages/d1/b6/7044ba6f27017923a143475fb4bf7e499fb59786bac55673192b0a35fbde/autoflake-2.2.0-py3-none-any.whl")
	version("2.2.1", sha256="265cde0a43c1f44ecfb4f30d95b0437796759d07be7706a2f70e4719234c0f79", expand=False, url="https://files.pythonhosted.org/packages/9e/a5/8471753bc95672fb16d9cd1cb82ba460c66721378dd8cc8629d86c148a09/autoflake-2.2.1-py3-none-any.whl")
	version("2.3.0", sha256="79a51eb8c0744759d2efe052455ab20aa6a314763510c3fd897499a402126327", expand=False, url="https://files.pythonhosted.org/packages/65/5b/859605af1b94acf8d1a65731b61ac3cba1ac97691e68b4963430f9553647/autoflake-2.3.0-py3-none-any.whl")
	version("2.3.1", sha256="3ae7495db9084b7b32818b4140e6dc4fc280b712fb414f5b8fe57b0a8e85a840", expand=False, url="https://files.pythonhosted.org/packages/a2/ee/3fd29bf416eb4f1c5579cf12bf393ae954099258abd7bde03c4f9716ef6b/autoflake-2.3.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-pyflakes", type=("build", "run"))

# {'pyflakes(>=1.1.0)': ['1.5.0', '1.5.1', '1.5.2', '1.5.3', '1.6.0', '1.6.1', '1.7.0', '1.7.1', '1.7.3', '1.7.4', '1.7.5'], 'toml(>=0.10.2)': ['1.5.0', '1.5.1', '1.5.2', '1.5.3'], 'tomli(>=2.0.1);python_version<"3.11"': ['1.6.0', '1.6.1', '1.7.0', '1.7.1', '1.7.3', '1.7.4', '1.7.5'], 'pyflakes>=1.1.0': ['1.7.5', '1.7.6', '1.7.7'], "tomli>=2.0.1;python_version<'3.11'": ['1.7.5', '1.7.6', '1.7.7', '1.7.8', '2.0.0', '2.0.1', '2.0.2', '2.1.0', '2.1.1', '2.2.0', '2.2.1', '2.3.0', '2.3.1'], 'pyflakes<3,>=1.1.0': ['1.7.8'], 'pyflakes>=3.0.0': ['2.0.0', '2.0.1', '2.0.2', '2.1.0', '2.1.1', '2.2.0', '2.2.1', '2.3.0', '2.3.1']}