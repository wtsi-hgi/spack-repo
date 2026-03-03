# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyJupyterContribNbextensions(PythonPackage):
	"""A collection of Jupyter nbextensions."""
	
	homepage = "https://github.com/ipython-contrib/jupyter_contrib_nbextensions.git"
	pypi = "jupyter-contrib-nbextensions/jupyter_contrib_nbextensions-0.7.0.tar.gz" 

	version("0.1.0", sha256="c4dd8cf259a17e8024e292bfd99c064c753a020221535e7074a4641a28c253ae", expand=False, url="https://files.pythonhosted.org/packages/ef/42/1c965d419c9b12b50b69c37e2954b185938ab0f1ce96fe42497ed9e7a759/jupyter_contrib_nbextensions-0.1.0-py2.py3-none-any.whl")
	version("0.2.0", sha256="9a638df07a48f52116ed10002037f54bb6d8f8d6d18e648f1d7e5e3be124b77e", expand=False, url="https://files.pythonhosted.org/packages/a4/83/1f9454ee53ab1f8c1c9565433ea03fe3e39ab04ac148b867dafe432a4f66/jupyter_contrib_nbextensions-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="b6ef7048042bdc8bb4708b4ddf233f09bec6a2a5a128eea20a9f81384978725d", expand=False, url="https://files.pythonhosted.org/packages/03/e4/adcc7982d2666de0551f4d2e487b0cb0516b579a2dabe1a4ad7fa0e4116e/jupyter_contrib_nbextensions-0.2.1-py2.py3-none-any.whl")
	version("0.2.2", sha256="f730bca64a0ef97bf354b158d3604620982dc8417fef6fee49f02d67d61b7d83", expand=False, url="https://files.pythonhosted.org/packages/d2/7d/2c79a479c96d86c047010fde55f7e7cbe543434734ceda392759bd4901c1/jupyter_contrib_nbextensions-0.2.2-py2.py3-none-any.whl")
	version("0.2.3", sha256="2d0c8c3276f436ddac09e2eb3ab6f1f805489d49744e73bfc14fdefe5c7394ba", expand=False, url="https://files.pythonhosted.org/packages/04/4b/fc09a9140be1c2548b50d8fae04785028229f5fc2d9b09320a9e36ca62b5/jupyter_contrib_nbextensions-0.2.3-py2.py3-none-any.whl")
	version("0.2.4", sha256="9d03d51545b317219f4a981fa21c1a03cd79636ebe3fe19c66c80fa2b06fa194", expand=False, url="https://files.pythonhosted.org/packages/68/46/6ad4522e193f1e0b02380bfe32722ff1e149f315398fa6a8e291c27ad3ae/jupyter_contrib_nbextensions-0.2.4-py2.py3-none-any.whl")
	version("0.2.5", sha256="2235b44d4e8bdcd1389fdfa4c688a3a61bf08c22790a8184095ef9350a2d42c1", expand=False, url="https://files.pythonhosted.org/packages/e4/2c/cf2798b5056d858b1dee41988379b7336a55e766ae9076c9e73a202306e1/jupyter_contrib_nbextensions-0.2.5-py2.py3-none-any.whl")
	version("0.2.6", sha256="46fd0a45b8f621bbe1025e9a6a5f40f84dc9a267e395fe926be1870b488e77d3", expand=False, url="https://files.pythonhosted.org/packages/80/94/6ba19e879f1bde85678ac3edd2150d2375498ec175d8d36f52e5f9a8f38d/jupyter_contrib_nbextensions-0.2.6-py2.py3-none-any.whl")
	version("0.2.7", sha256="70cfdda4996c0c7532ccdd10cdf95f195c73c1dc0617c5ea9267abd442cfdf3d")
	version("0.2.8", sha256="db75475d47b2a388d86bb17a557fba7aff49cc17d07157c41ac07d9c1ed01347", expand=False, url="https://files.pythonhosted.org/packages/de/c6/7ce7575de5091edd6aa2ce00ee9eefcc6679eace34189940e931c2bad61c/jupyter_contrib_nbextensions-0.2.8-py2.py3-none-any.whl")
	version("0.3.0", sha256="b45dbeb707a61278d53c2d598bf611b17ac450c98cff9f481fb9ad565ea93897", expand=False, url="https://files.pythonhosted.org/packages/62/f3/ba9660feb54721f364c3300282d99b4a2140a2f7d1e5d2615d01f407157a/jupyter_contrib_nbextensions-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="d2aca469da9b7a438faf94a887c59d03a42cf0f695d1c1a35e43b32689d3caae", expand=False, url="https://files.pythonhosted.org/packages/32/98/98268c3be94fc1b371bdb6568ec4c3c642174461615c467829c59fe88344/jupyter_contrib_nbextensions-0.3.1-py2.py3-none-any.whl")
	version("0.3.2", sha256="8e5aae4ed85e887b1ee69ffba190e78298e81592ff86f58649eaddcf5ab59a2f")
	version("0.3.3", sha256="9b697eb6e73573050a5de8fd48abff0c27cf0563c74b4757758ba78b9d3c9299", expand=False, url="https://files.pythonhosted.org/packages/54/ed/d53544d2d4a0e83a4e4d2e7ae4ce1ac230bc52d36cff1e274b248a64304b/jupyter_contrib_nbextensions-0.3.3-py2.py3-none-any.whl")
	version("0.4.0", sha256="fd26224ed2ff2436da5cef95243e910d581821417ae958f21499d8e5b87687e0", expand=False, url="https://files.pythonhosted.org/packages/8f/f9/e7868ef7eda5a3a5dc03c4cdb3649c568c75b1b5fe5dbf2266cd30168f79/jupyter_contrib_nbextensions-0.4.0-py2.py3-none-any.whl")
	version("0.5.0", sha256="f4893d99fed6be6587cd2c722ef8841556283a697a482288b621b514beda2405", expand=False, url="https://files.pythonhosted.org/packages/d2/f1/57cd4d05d7f070e662844a925d6f6d726ecaf93d8cc2d7b56a66c765fb42/jupyter_contrib_nbextensions-0.5.0-py2.py3-none-any.whl")
	version("0.5.1", sha256="2c071f0aa208c569666f656bdc0f66906ca493cf9f06f46db6350db11030ff40", expand=False, url="https://files.pythonhosted.org/packages/33/f0/6e2c00afda860f655fbf0f795f7310bdbf12122846344dfdc803fc7455d5/jupyter_contrib_nbextensions-0.5.1-py2.py3-none-any.whl")
	version("0.7.0", sha256="06e33f005885eb92f89cbe82711e921278201298d08ab0d886d1ba09e8c3e9ca")

	depends_on("py-setuptools", type=("build", "run"))
