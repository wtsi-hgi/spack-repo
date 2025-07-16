# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlaskSock(PythonPackage):
	"""WebSocket support for Flask"""
	
	homepage = "https://github.com/miguelgrinberg/flask-sock"
	pypi = "flask-sock/flask_sock-0.7.0-py3-none-any.whl" 

	version("0.0.1", sha256="a217dbee85f2b82a4a21eeb04804d20ae4eccd3543873eb18c20465afbc529a2", expand=False, url="https://files.pythonhosted.org/packages/3d/79/d1402b844ce5dc890feb07966482655b4fdaf110696fde8cb791467c9398/flask_sock-0.0.1-py2.py3-none-any.whl")
	version("0.0.2", sha256="302d0295b31025d7284bf34d5fdc56e0f1c3430e9a9c5a522b0a37f3006b2c75", expand=False, url="https://files.pythonhosted.org/packages/40/ed/a7c08f19fe72dd44611d75152d91ddb2741864619535047161b3344fd210/flask_sock-0.0.2-py2.py3-none-any.whl")
	version("0.0.3", sha256="3bc20d78fb57ac380b328db857c09db8035170a37d7750fe5c69d6ce369278fb", expand=False, url="https://files.pythonhosted.org/packages/f1/fb/f57be6434e8bb1e46c78b172a5c57addf15d0f0209557ceee5a4856f172d/flask_sock-0.0.3-py3-none-any.whl")
	version("0.0.4", sha256="0c73e2c14ca3b6bb5856f6bdb78549bb1506d1ec253d6bd266924e729b473a94", expand=False, url="https://files.pythonhosted.org/packages/86/a3/f04d04b1b97bcf4e9dd31a6430ec7c8d1ff9ab3f114122627081b6718043/flask_sock-0.0.4-py3-none-any.whl")
	version("0.0.5", sha256="a7f7d6a41fd72f221c331a0110d3dbacce8e135fa97d1cac9bc43ceff159a9ea", expand=False, url="https://files.pythonhosted.org/packages/0f/12/11362c2a3a16a0de837158df00f44e47a8c06506df11199b3e3a3406dc31/flask_sock-0.0.5-py3-none-any.whl")
	version("0.1.0", sha256="323a23fba0c0b08c8e3a936aa51f5327771228cdcc1ff824534895c99ba1f182", expand=False, url="https://files.pythonhosted.org/packages/85/c4/22c8a49c5d1f5ff97eca6002569fc88679267290162277f7bd03b76d6131/flask_sock-0.1.0-py3-none-any.whl")
	version("0.2.0", sha256="ef1c242107e992ebff6acbd203d34d24184f9e4a23bd4c9a598380a548a46173", expand=False, url="https://files.pythonhosted.org/packages/a9/00/da5cd78d87ca956a0e618f0436120f1c3ce3316bd4b37c3686c15ba2272f/flask_sock-0.2.0-py3-none-any.whl")
	version("0.3.0", sha256="9355d8b144fed1309cea6653d678aa777bbfc2e44ae7a5a767fe15281f115b35", expand=False, url="https://files.pythonhosted.org/packages/3c/d0/08dcf953238babf96de3e0a1a624ba9bbd88761cd6449bdb42bd97cb734c/flask_sock-0.3.0-py3-none-any.whl")
	version("0.4.0", sha256="f2a21916f4758c7da8e1c2f3561df4502251ebfb035232898c40f64b99e94bf8", expand=False, url="https://files.pythonhosted.org/packages/d5/af/26b5c2e4be8b777aa044a76233b82fd4b0df594de2475d1e2938349d79ce/flask_sock-0.4.0-py3-none-any.whl")
	version("0.5.0", sha256="4d0fd22a40bdf586e2e9dfcf6ea11ee25036167d6e81e38f94d9900d416bdc3e", expand=False, url="https://files.pythonhosted.org/packages/ae/4f/3eb76fa76cb9e2c863c48ada8b0eb5da2e3d36afc582e04c8367a4929b56/flask_sock-0.5.0-py3-none-any.whl")
	version("0.5.1", sha256="c78eb9b8d7b7e9c44a625b58cd70cea0126b674c5c474b96b24e398ba2370a9a", expand=False, url="https://files.pythonhosted.org/packages/88/86/016672e243f0edbef28680d8a69de04d4736af78e098a3f630ff9cf656ed/flask_sock-0.5.1-py3-none-any.whl")
	version("0.5.2", sha256="bdd60520d031eb92e6fa2dbd3deffbb6e71d3662e9d39bfe53d2eccf971d0fd0", expand=False, url="https://files.pythonhosted.org/packages/3c/e8/cd38da6c66432ba6d2544f40cdf90189af4b1d8460ce428af032e7eabc31/flask_sock-0.5.2-py3-none-any.whl")
	version("0.6.0", sha256="593fffb186928080a5b5b03d717efc56dac2d5ed690ce6bfff333b3597a2f518", expand=False, url="https://files.pythonhosted.org/packages/9a/74/f36e2882d19f0f3e99ec43fe8d2c599f674f332c3ed9bb94cd3c6b987573/flask_sock-0.6.0-py3-none-any.whl")
	version("0.7.0", sha256="caac4d679392aaf010d02fabcf73d52019f5bdaf1c9c131ec5a428cb3491204a", expand=False, url="https://files.pythonhosted.org/packages/d8/98/107728ce3f430b5481eb426ccc5e1f7c8ab0bd01eaf231c62a8d528ff721/flask_sock-0.7.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-flask", type=("build", "run"))
	depends_on("py-simple-websocket", type=("build", "run"))

# {'flask': ['0.0.1', '0.0.2'], 'werkzeug(>=2.0.0rc3)': ['0.0.1', '0.0.2'], 'wsproto': ['0.0.2', '0.0.4', '0.0.5', '0.1.0', '0.2.0'], 'simple-websocket': ['0.3.0', '0.4.0'], 'flask(>=2)': ['0.4.0', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'simple-websocket(>=0.5.1)': ['0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'flask>=2': ['0.7.0'], 'simple-websocket>=0.5.1': ['0.7.0'], "sphinx;extra=='docs'": ['0.7.0']}