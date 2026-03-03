# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyXdg(PythonPackage):
	"""Variables defined by the XDG Base Directory Specification"""
	
	homepage = "https://github.com/srstevenson/xdg-base-dirs"
	pypi = "xdg/xdg-6.0.0-py3-none-any.whl" 

	version("1.0.1", sha256="02c2a1bcd43d451840c1a76a4e87bc8d4a57dd5023e73eb794732cb68d104d5b", expand=False, url="https://files.pythonhosted.org/packages/6b/13/0c2f44c118eb5f53218fb70d793590392c6787c3d9015c546c3554f73b83/xdg-1.0.1-py2.py3-none-any.whl")
	version("1.0.3", sha256="37c7963c30251baa36a74821bd5ed0e921181a62c075cc6f7a125f950b4ef974", expand=False, url="https://files.pythonhosted.org/packages/d1/67/fb4c192da59213d4a6f3e10057001af92ea1510439fa05d87bc2d7be1b2f/xdg-1.0.3-py2.py3-none-any.whl")
	version("1.0.4", sha256="a1961f129f93c32724b7ae66a2ad3af5798e8a3a8b9c02bd41f99b5e75cde511", expand=False, url="https://files.pythonhosted.org/packages/e7/2b/0970a9bfb4e9e23dbe08b25ce732d0a878c222bd83afbbe02980d6c800cf/xdg-1.0.4-py2.py3-none-any.whl")
	version("1.0.5", sha256="1f96d99924e5906d6688ba0f999d972db5b479c106bb2da6d685581a4d0e5cb6", expand=False, url="https://files.pythonhosted.org/packages/99/83/4cf440812e74917d06180631559e869986cb53df8bf8225a8972c4491e75/xdg-1.0.5-py2.py3-none-any.whl")
	version("1.0.6", sha256="34e1ea24ffefb8482639ad9266f7edddc601b2bfad844a189df1c49bf1fd75f4", expand=False, url="https://files.pythonhosted.org/packages/5c/2a/95266a51b9a67155c929518f092217eee8a826fa90e5d9e15f400ed1ed89/xdg-1.0.6-py2.py3-none-any.whl")
	version("1.0.7", sha256="4b4aaeefb4a94590a17b2e1aba32cac7babd45af5b3bcf89844b17ea13821555", expand=False, url="https://files.pythonhosted.org/packages/79/5a/c8e3f778998c3aedc74b55dff2852fe5952eac115bcf53adcb8565031435/xdg-1.0.7-py2.py3-none-any.whl")
	version("2.0.0", sha256="83fb55b3ba957f8eb5dec17afce3c1bc625ee2ef24aa3f5fa453d696a4669c10", expand=False, url="https://files.pythonhosted.org/packages/d9/22/4bbfb927cae2bbc2c5b047a27480f28ca788f4689fe3399722d4c963d35f/xdg-2.0.0-py2.py3-none-any.whl")
	version("3.0.0", sha256="e202a32caebf269ade0ac8835ffa43250bf10c2a1eb8f57f6d252067df690e57", expand=False, url="https://files.pythonhosted.org/packages/19/e3/084a476eb03f3203eacf2c83d1d062fe5ec47589cb6428c6464f83d2e962/xdg-3.0.0-py2.py3-none-any.whl")
	version("3.0.1", sha256="74beff687ee958a9df70c476bce94fb8a3b77879c7c47b46e3c6c3d89c0c7862", expand=False, url="https://files.pythonhosted.org/packages/6d/8e/811fbbf7dfab9570dc8e8fab43e6c1977248a15e461f4bd96b9791b85463/xdg-3.0.1-py2.py3-none-any.whl")
	version("3.0.2", sha256="1436ed336bdb9e5bede813eb590dd6a67d21f78b16aba1f5ba646b976225652e", expand=False, url="https://files.pythonhosted.org/packages/cc/7e/10b63c5d0546fc168ced3465c520b00de698d960e1c74800aea2a777aa8e/xdg-3.0.2-py2.py3-none-any.whl")
	version("4.0.0", sha256="4033f807e13f6966add123c5961e0e59c95fd0ab3f70c748e45e5d3433424024", expand=False, url="https://files.pythonhosted.org/packages/c5/42/79a2343668eba91827a18533f917b2c451bd91e34670474a7bca610e217b/xdg-4.0.0-py3-none-any.whl")
	version("4.0.1", sha256="bf9032b027e3061d38c362a21b14dcf057a5b5a4906956f8e8278cefdf73f38b", expand=False, url="https://files.pythonhosted.org/packages/cd/7b/6ad85311fd715df37ef9bb17ad1b26e26b4cdd69c7e1e7e285422b83a7e1/xdg-4.0.1-py3-none-any.whl")
	version("5.0.0", sha256="a76fda30b171b75519cfbf1c39f29b1006f2c1638d6e4f6b39d8c5525672a678", expand=False, url="https://files.pythonhosted.org/packages/1d/18/c74c79dc676d878448cc0fa7fe15b74a1782566e42c61eec531c20c9d581/xdg-5.0.0-py3-none-any.whl")
	version("5.0.1", sha256="9ddd6649bee9148f952305603a08474e3ef37c909eb19dfcb9737d54ebcc407e", expand=False, url="https://files.pythonhosted.org/packages/be/eb/a4669d56ce4934d88a163e4b0d3cbc96606c073100bd6031f7972679877b/xdg-5.0.1-py3-none-any.whl")
	version("5.0.2", sha256="d59c8a0c24293491a0a3325eb1beb7a9b03e0802385c2759ed9c19cd34602ddc", expand=False, url="https://files.pythonhosted.org/packages/34/d2/06c652db79ec7d27df2eee9d30963488cb2f2554705256022b73d917c5c4/xdg-5.0.2-py3-none-any.whl")
	version("5.1.0", sha256="eb021156d2e1897e3cfe16bc0cd7aee6dd8157c8015a4cfbf4b495ed730226e6", expand=False, url="https://files.pythonhosted.org/packages/33/f0/48eaf3d8c8123ee5aa92fde45c6f5dab22c9e21789c378292c631f38b0e0/xdg-5.1.0-py3-none-any.whl")
	version("5.1.1", sha256="865a7b56ed1d4cd2fce2ead1eddf97360843619757f473cd90b75f1817ca541d", expand=False, url="https://files.pythonhosted.org/packages/ea/09/4a0f30aada49e142b94bbb232c023abcbc6ced7e2a9776533fb14977e9db/xdg-5.1.1-py3-none-any.whl")
	version("6.0.0", sha256="df3510755b4395157fc04fc3b02467c777f3b3ca383257397f09ab0d4c16f936", expand=False, url="https://files.pythonhosted.org/packages/dd/54/3516c1cf349060fc3578686d271eba242f10ec00b4530c2985af9faac49b/xdg-6.0.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:4.0", type=("build", "run"))
