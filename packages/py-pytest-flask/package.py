# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPytestFlask(PythonPackage):
	"""A set of py.test fixtures to test Flask applications."""
	
	homepage = "https://github.com/pytest-dev/pytest-flask"
	pypi = "pytest-flask/pytest_flask-1.3.0-py3-none-any.whl" 

	version("0.10.0-py2.7", sha256="657c7de386215ab0230bee4d76ace0339ae82fcbb34e134e17a29f65032eef03", expand=False, url="https://files.pythonhosted.org/packages/30/39/cfff2ef18c97f50024ee4bcb8a1ab5ec7dabdb2c2edc5b2cc93e8f867481/pytest_flask-0.10.0-py2.py3-none-any.whl")
	version("0.11.0", sha256="fbf77a4ff2efdaa15d895af00625d8242f4bbdf10aceaefc9deb170bb7a45767", expand=False, url="https://files.pythonhosted.org/packages/1b/70/7f323b4ffe0a3a30c0b46bc3ce117ff67b7152eafb82690cab049b089e8a/pytest_flask-0.11.0-py2.py3-none-any.whl")
	version("0.12.0", sha256="be3551e5d8cccd2f26e51fa4268398619be18b9e2300fdab7f4b2aeaeee0a588", expand=False, url="https://files.pythonhosted.org/packages/df/4d/d0b09e1c0862b70013061084b85c34778931f9655492c0077de17ebe5284/pytest_flask-0.12.0-py2.py3-none-any.whl")
	version("0.13.0", sha256="959f01a2e6121d4208263f571bf2de24aa89ebf2f752b15824e4e597fa35bb7e", expand=False, url="https://files.pythonhosted.org/packages/79/6d/17d55937f9f71032a118c9649cdd00ea94a22714f57ce7e1a885df90a459/pytest_flask-0.13.0-py2.py3-none-any.whl")
	version("0.14.0", sha256="e9b120d23f73e0495d8fa1bc3b580b18cc9f98b8d6808bc45fdbcbab7d718242", expand=False, url="https://files.pythonhosted.org/packages/52/a8/3fab52af3688311921205439e3e543b2b1fcce0e3c8acd2cad8061ecfe4f/pytest_flask-0.14.0-py2.py3-none-any.whl")
	version("0.15.0", sha256="283730b469604ecb94caac28df99a40b7c785b828dd8d3323596718b51dfaeb2", expand=False, url="https://files.pythonhosted.org/packages/a4/3b/d88d4140df2e89543b46a3373393954f7f67eef30f7154c885e72dc6e7ea/pytest_flask-0.15.0-py2.py3-none-any.whl")
	version("0.15.1", sha256="9001f6128c5c4a0d243ce46c117f3691052828d2faf39ac151b8388657dce447", expand=False, url="https://files.pythonhosted.org/packages/03/b8/90437a7acaf0d695bdd0dd6f575ff131808202ec0d618c6818e2e1c8c7a0/pytest_flask-0.15.1-py2.py3-none-any.whl")
	version("0.3.1-py2.7", sha256="b360945dabad71d10a5b5dc5a6bc08b83f3bb8618f68f9a0084529e415255709", expand=False, url="https://files.pythonhosted.org/packages/0b/92/28c6f2cbc59b722b918e10628cb748e93d7f6401cf87c331ea8d7f6eb257/pytest_flask-0.3.1-py2.py3-none-any.whl")
	version("0.3.2-py2.7", sha256="e8ac34838b7257bee3b52e23dd0c4d79fda3fe90a2aa18de3891ad5428741d02", expand=False, url="https://files.pythonhosted.org/packages/05/e1/f601549f7541fb6b4ad6590d9493b44dc3e779011e366ef0d631134ee475/pytest_flask-0.3.2-py2.py3-none-any.whl")
	version("0.3.3-py2.7", sha256="976f3cf859fb93aae2773e6779b3f8389bf79bc72ffa6c468ebe4955ce0ce9d0", expand=False, url="https://files.pythonhosted.org/packages/39/f7/1d4118c156371859068e900d239b44f8074f8417cb4c6ae5a482b4ccbdf6/pytest_flask-0.3.3-py2.py3-none-any.whl")
	version("0.3.4-py2.7", sha256="0f099043f22b9acb291243e0d89e1f086cfb3144e4d8e7ce2015c9f8f4ea4d08", expand=False, url="https://files.pythonhosted.org/packages/4e/fd/2d657292ee9f7f3ac3a0b76c2234dd4ac0c443533a044cab91c750be8697/pytest_flask-0.3.4-py2.py3-none-any.whl")
	version("0.4.0-py2.7", sha256="450ffe48694a0cfb83f6f9a03c89800f16e7aaf13dbd3784045626b672dcf65b", expand=False, url="https://files.pythonhosted.org/packages/29/77/02c8f9097213607efcd53d98b8b1189c391745bfdf31821acbe302650168/pytest_flask-0.4.0-py2.py3-none-any.whl")
	version("0.5.0-py2.7", sha256="e9edc999173866959f2ba8f1979c722b13a4dfb8a97fe074d874f15e985a232f", expand=False, url="https://files.pythonhosted.org/packages/a4/d3/a97b1e9aa176f3f22b8d2458d4c50402654bc616b3c8ef9748d51876e070/pytest_flask-0.5.0-py2.py3-none-any.whl")
	version("0.6.0-py2.7", sha256="490f72ee5a1743e6ad424833a6770b864e53d198cb4ea25175e1771550c72772", expand=False, url="https://files.pythonhosted.org/packages/ec/3e/fdf17a734837d09b0bf09870a237053cf665ee1fffe693c11d0a23bfb992/pytest_flask-0.6.0-py2.py3-none-any.whl")
	version("0.6.1-py2.7", sha256="68baef20fcbe3f9187dc6e3197e53e1dd2635026e3475d92c8b31d7091ce5350", expand=False, url="https://files.pythonhosted.org/packages/4d/06/1d9aac7916f24c8aaefc4c91d4065c2dd53f0e33f0a6859743d538528d98/pytest_flask-0.6.1-py2.py3-none-any.whl")
	version("0.6.2-py2.7", sha256="a42078b1eeef345849a0663e5ac24fe77cff6c70e647d911f303e308b3c4d99f", expand=False, url="https://files.pythonhosted.org/packages/d2/14/566b62165d232c35af980fd6a9d2161143976364def833437e73da40433c/pytest_flask-0.6.2-py2.py3-none-any.whl")
	version("0.6.3-py2.7", sha256="647218259f40f9a0584f89d82c6bb650ee6883bb243fe1ab64ee2bb1eaf17bde", expand=False, url="https://files.pythonhosted.org/packages/9f/2e/902e3d1adf0e0e3875f8f84b134f8e592312c94376ac5f643d636c1b4dfe/pytest_flask-0.6.3-py2.py3-none-any.whl")
	version("0.7.0-py2.7", sha256="c317425aa07ad6e07863c6c989f30a7654eb8bbc972910419662067674b29647", expand=False, url="https://files.pythonhosted.org/packages/11/0d/b6f15507e46f314de1f47b9317e73700742250bd0370a05798ddc1fc05fe/pytest_flask-0.7.0-py2.py3-none-any.whl")
	version("0.7.1-py2.7", sha256="69772fc449af3601956b0725d7239960c80abad04423253bf9b37f06f4867c00", expand=False, url="https://files.pythonhosted.org/packages/34/aa/067b82ad695accee398bfecac73a0783e86820bf5169bd55a6a4a349a4f4/pytest_flask-0.7.1-py2.py3-none-any.whl")
	version("0.7.2-py2.7", sha256="e1c1a2a7b78f6f00bef51dbe395897fac8324e3e997b91dcc59efa547ca966ce", expand=False, url="https://files.pythonhosted.org/packages/7e/ef/c8ecd7381a25d2206ddbed2f95a15471c48a8ab3a4022cf92c9b1298baf9/pytest_flask-0.7.2-py2.py3-none-any.whl")
	version("0.7.3-py2.7", sha256="e92a62382e2b16fcae19209b9f62102ca0295c54c3cfafdc6e44fdc2b16c4e4a", expand=False, url="https://files.pythonhosted.org/packages/9a/8d/f3b2706268b2f70156416a5b8af865efd13fd470cd705dcf4befb8058e5d/pytest_flask-0.7.3-py2.py3-none-any.whl")
	version("0.7.4-py2.7", sha256="d7a313790f87894875d99082b25832da859fa29cfd7708f2e4a95a7a02f55ff4", expand=False, url="https://files.pythonhosted.org/packages/15/2d/e4451dbdd6727fb18e42c1eee84ad1ef243c6abd4711bf2bd63dcc619972/pytest_flask-0.7.4-py2.py3-none-any.whl")
	version("0.7.5-py2.7", sha256="4da096512392bef6b7d5016fdbcd55d522276ba834be55b76a3423e2de7cdb9d", expand=False, url="https://files.pythonhosted.org/packages/0d/c4/2a58394bb31a336bbcd8352cfd7960a999fb640edd8c10084b0570942a4f/pytest_flask-0.7.5-py2.py3-none-any.whl")
	version("0.8.0-py2.7", sha256="30222372969cffe94f19b8a7fe1f1a9e87e24d0b25d5b066e53d45fb9aec5977", expand=False, url="https://files.pythonhosted.org/packages/28/d6/a58c6a34e59781b9dbe8c4510ab928a7374bb1a41421c9beccb630e2621c/pytest_flask-0.8.0-py2.py3-none-any.whl")
	version("0.8.1-py2.7", sha256="143fe1704a991a611e1a6ff48fb3911129b8fa59cd04a0bfb5a9b1153c697d36", expand=False, url="https://files.pythonhosted.org/packages/c6/89/beb648a7684a3e32a878aa7e0b8f3c180e2b764775061abd0dab36415b71/pytest_flask-0.8.1-py2.py3-none-any.whl")
	version("0.9.0-py2.7", sha256="7a941ae2bfcc3c02e5292f73513ede8c17e58d951411156068c5c09d3db34285", expand=False, url="https://files.pythonhosted.org/packages/cd/98/48a1e25456b9910d60cc56423e2971ad53e0b7a2a9a0b746491cae131dd7/pytest_flask-0.9.0-py2.py3-none-any.whl")
	version("1.0.0", sha256="44948d3feab48c69e89b087129cc4db66bad9cb5aa472c08dfc798c69f4eac67", expand=False, url="https://files.pythonhosted.org/packages/51/4f/af696c59f49ddf134c04b705d28988011d7b9f58c1f319d2bad4f1d76e8b/pytest_flask-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="28a24a5c12778f6e2b12eaf825e71944210aaba061edbd2c3e15e3664bc15407", expand=False, url="https://files.pythonhosted.org/packages/b8/46/369ae5134b07d5339ca4438071e62b3d354b80bdc96be63858b63711c71f/pytest_flask-1.1.0-py3-none-any.whl")
	version("1.2.0", sha256="fe25b39ad0db09c3d1fe728edecf97ced85e774c775db259a6d25f0270a4e7c9", expand=False, url="https://files.pythonhosted.org/packages/09/b4/a84a43b638d7f6d68c2eb092a5b6c8127fc873eac166538b2d0010a4e948/pytest_flask-1.2.0-py3-none-any.whl")
	version("1.3.0", sha256="c0e36e6b0fddc3b91c4362661db83fa694d1feb91fa505475be6732b5bc8c253", expand=False, url="https://files.pythonhosted.org/packages/de/03/7a917fda3d0e96b4e80ab1f83a6628ec4ee4a882523b49417d3891bacc9e/pytest_flask-1.3.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-werkzeug", type=("build", "run"))
	depends_on("py-pytest", type=("build", "run"))
	depends_on("py-flask", type=("build", "run"))
	depends_on("python@2..7", when="@0.10.0-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.3.1-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.3.2-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.3.3-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.3.4-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.4.0-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.5.0-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.6.0-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.6.1-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.6.2-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.6.3-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.7.0-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.7.1-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.7.2-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.7.3-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.7.4-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.7.5-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.8.0-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.8.1-py2.7", type=("build", "run"))
	depends_on("python@2..7", when="@0.9.0-py2.7", type=("build", "run"))

# {'Flask': ['0.10.0-py2.7', '0.11.0', '0.12.0', '0.13.0', '0.14.0', '0.15.0', '0.15.1', '0.3.1-py2.7', '0.3.2-py2.7', '0.3.3-py2.7', '0.3.4-py2.7', '0.4.0-py2.7', '0.5.0-py2.7', '0.6.0-py2.7', '0.6.1-py2.7', '0.6.2-py2.7', '0.6.3-py2.7', '0.7.0-py2.7', '0.7.1-py2.7', '0.7.2-py2.7', '0.7.3-py2.7', '0.7.4-py2.7', '0.7.5-py2.7', '0.8.0-py2.7', '0.8.1-py2.7', '0.9.0-py2.7', '1.0.0', '1.1.0', '1.2.0', '1.3.0'], 'Werkzeug(>=0.7)': ['0.10.0-py2.7', '0.11.0', '0.12.0', '0.13.0', '0.14.0', '0.15.0', '0.15.1', '0.3.3-py2.7', '0.3.4-py2.7', '0.4.0-py2.7', '0.5.0-py2.7', '0.6.0-py2.7', '0.6.1-py2.7', '0.6.2-py2.7', '0.6.3-py2.7', '0.7.0-py2.7', '0.7.1-py2.7', '0.7.2-py2.7', '0.7.3-py2.7', '0.7.4-py2.7', '0.7.5-py2.7', '0.8.0-py2.7', '0.8.1-py2.7', '0.9.0-py2.7', '1.0.0', '1.1.0', '1.2.0'], 'pytest(>=2.4)': ['0.10.0-py2.7', '0.3.3-py2.7', '0.3.4-py2.7', '0.4.0-py2.7', '0.5.0-py2.7', '0.6.0-py2.7', '0.6.1-py2.7', '0.6.2-py2.7', '0.6.3-py2.7', '0.7.0-py2.7', '0.7.1-py2.7', '0.7.2-py2.7', '0.7.3-py2.7', '0.7.4-py2.7', '0.7.5-py2.7', '0.8.0-py2.7', '0.8.1-py2.7', '0.9.0-py2.7'], "Sphinx;extra=='docs'": ['0.10.0-py2.7', '0.11.0', '0.12.0', '0.13.0', '0.14.0', '0.15.0', '0.15.1', '0.7.0-py2.7', '0.7.1-py2.7', '0.7.2-py2.7', '0.7.3-py2.7', '0.7.4-py2.7', '0.7.5-py2.7', '0.8.0-py2.7', '0.8.1-py2.7', '0.9.0-py2.7', '1.0.0', '1.1.0', '1.2.0', '1.3.0'], "sphinx-rtd-theme;extra=='docs'": ['0.10.0-py2.7', '0.11.0', '0.12.0', '0.13.0', '0.14.0', '0.15.0', '0.15.1', '0.7.0-py2.7', '0.7.1-py2.7', '0.7.2-py2.7', '0.7.3-py2.7', '0.7.4-py2.7', '0.7.5-py2.7', '0.8.0-py2.7', '0.8.1-py2.7', '0.9.0-py2.7', '1.0.0', '1.1.0', '1.2.0', '1.3.0'], 'pytest': ['0.11.0', '0.12.0', '0.13.0', '0.14.0', '0.15.0', '0.15.1', '0.3.1-py2.7', '0.3.2-py2.7'], 'pytest(>=3.6)': ['0.12.0', '0.13.0', '0.14.0', '0.15.0', '0.15.1'], 'pytest(>=5.2)': ['1.0.0', '1.1.0', '1.2.0'], 'pytest>=5.2': ['1.3.0'], 'Werkzeug': ['1.3.0']}