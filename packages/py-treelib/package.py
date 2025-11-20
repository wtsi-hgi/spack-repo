# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTreelib(PythonPackage):
	"""A Python implementation of tree structure."""
	
	homepage = "https://github.com/caesar0301/treelib"
	pypi = "treelib/treelib-1.8.0-py3-none-any.whl" 

	version("1.2", sha256="446cafd02cfcba65ed85e3373ae895dfe18db52ab4b3f58646763859f660418d")
	version("1.2.2", sha256="f479f660a2c4cc8d7fb9ca3a0fa16f0d0459580c6ea816a6fc2b924060b971eb")
	version("1.2.3", sha256="39d76cde41cc8ed98d586c136c12ceb97766dc436c11e75b190fb4315e8a19cd")
	version("1.2.4", sha256="fbeddbb03eb34a614cb926674b23135edb4774f4a6c3d1f37db4db8b9ab8e4a6")
	version("1.2.5", sha256="f49f9b46ced0162dc7241385ba6efe3767cb3e60c1989d024ce3ca37c7f4ff57")
	version("1.2.6", sha256="1f6897f9c5067f1eca6c50cba5c7e893b3c938f0dcd5fed559e0ca27d4db810e")
	version("1.2.7", sha256="75ebe90135411bbfbedeb6835e5566b448f9962024e50f6dda59a09fece980fa")
	version("1.2.7b", sha256="6303eea77d383b4e9db4b0cceb2aba5327d7b12fe158f79642dbd6a35657abff")
	version("1.2.8", sha256="d611b0ee551ca3b67fbd7457262148ebc2d08961c396fb0af6403d33b0e47860")
	version("1.3.0", sha256="2bb72b584f6480041c9dce66d58af11a94effa38f0749fb619d617571e10aa92")
	version("1.3.1", sha256="f007c53a161703389ac25945c31d5e537794be4441a3022e4a62ebbbaab69ff3")
	version("1.3.2", sha256="d63877c851da9dab46c2c065bbb619fe00a3f716aecc17e76c022b6f9075c365")
	version("1.3.5", sha256="176eeb6cd15895714a458a762dc54eaf7f9cbde70010136012f3781c63aeb967")
	version("1.3.7", sha256="157dfefcafaca41ed0605ae2ba4432fbec80f6bcfd5bb0c14fb756b24809329f")
	version("1.4.0", sha256="726f7b7445ee74e62af8e4a063467d6f305eae6cfe2f2756066370a8a7618a42")
	version("1.5.0", sha256="74638bc7976d2f19b0da05a047e9b85f26f9ac8381f99af3e2f765b2e878b1db")
	version("1.5.1", sha256="5f781a48eef400d09b5d57e786b1e1ac5e5127cd33f1399e7fd8066f1858e0e4")
	version("1.5.3", sha256="3e4ee4ea22ec9e6e5fe5df4f4d6189a9b2c6c6604bd835d692419466e0312f0a")
	version("1.5.5", sha256="8fa9461fe4ae835cbe40b57391ca051134b4eb1cc18606fa773b75815ff80144", expand=False, url="https://files.pythonhosted.org/packages/20/b2/421f24f0057da632e30db80e53b56c3f782bcccabff61e5c00b025c23d96/treelib-1.5.5-py2-none-any.whl")
	version("1.6.1", sha256="1cbfffb2d2b75ccac27d0200cee0507b6fbb0726e0afb9fae017ade5d2ce8788")
	version("1.6.3", sha256="2a7096d6b7e711bbc1e67f942430be7d7882e8c45b197bd1cbfb5cd35705b0cc", expand=False, url="https://files.pythonhosted.org/packages/89/9c/785a06eba694dac22aeae08e177da148474e49f1c8ecc521619a9a68bfc6/treelib-1.6.3-py3-none-any.whl")
	version("1.6.4", sha256="4218f7dded2448dfa6a335888bf68a28430660163e7faf18c6128ec4477d34c0", expand=False, url="https://files.pythonhosted.org/packages/99/36/0d5a284d58dee33a738c1a77cf032a93cb978a7382497fb54f31baa0dc1a/treelib-1.6.4-py3-none-any.whl")
	version("1.7.0", sha256="c37795eaba19f73f3e1a905ef3f4f0cab660dc7617126e8ae99391e25c755416", expand=False, url="https://files.pythonhosted.org/packages/74/93/0944bb5ade972a5ef2dd9211a20730081ed2833024239171807d7a9bd4b0/treelib-1.7.0-py3-none-any.whl")
	version("1.7.1", sha256="69aa12559c603273c77580cc86089021756654a754a7c674038de20f9daeafde", expand=False, url="https://files.pythonhosted.org/packages/01/da/66fb7b0f91a4329d5e0dd49a7464a1ced62a9d495362ae4c5cc055f268ba/treelib-1.7.1-py3-none-any.whl")
	version("1.8.0", sha256="5235d1ebf988c5026f26ce6e5e0cd470007f16d4978185f5c9b3eee8a25aef81", expand=False, url="https://files.pythonhosted.org/packages/2e/24/32361f5d0e2eff7ff1881ac6833b6b090cfe34515b1ee9082636cbe69442/treelib-1.8.0-py3-none-any.whl")

	depends_on("py-six", type=("build", "run"))

	@run_after("install")
	def install_test(self):
		self.spec["python"].command("-c", "import treelib")
