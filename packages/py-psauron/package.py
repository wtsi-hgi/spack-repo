# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPsauron(PythonPackage):
	"""A tool to assess protein coding gene annotation"""
	
	homepage = "https://github.com/Markusjsommer/psauron"
	pypi = "psauron/psauron-1.0.8-py3-none-any.whl" 

	version("1.0.5", sha256="bced768bf31bbf338fb57e1649ed926bbc3d4bc53a8a9d9dc356a555023a8326", expand=False, url="https://files.pythonhosted.org/packages/a5/24/0df0cc080d5132c6777793d0ba7520f438645b4cf051701d246d8cf863f8/psauron-1.0.5-py3-none-any.whl")
	version("1.0.6", sha256="294dfeeb6e312d3df5a555850fc60e666904ab2898c6d61813265c66f1bd4b7d", expand=False, url="https://files.pythonhosted.org/packages/ee/cd/e52399011b5968382bc60d3981edcf310933c315c11c07536d749608f350/psauron-1.0.6-py3-none-any.whl")
	version("1.0.7", sha256="051c2f69df192037f4fac71f16a187fe973ec6c0c961be5168301fb7d257a0e9", expand=False, url="https://files.pythonhosted.org/packages/3a/3a/9a7fbd78b57ae281d3c88d93cad0f2547f38287f0672baeef190f70e005d/psauron-1.0.7-py3-none-any.whl")
	version("1.0.8", sha256="69883231e93c09c3cd49a1ff33d8be6096cbfbc9ae32d00462c7e334cc75cd28", expand=False, url="https://files.pythonhosted.org/packages/8f/8d/b445ebad813786dd947df601b128e2b5cfe61bf418f6d9110f4424d447bc/psauron-1.0.8-py3-none-any.whl")

	depends_on("python@3.9:3.13", type=("build", "run"))
	depends_on("py-torch", type=("build", "run"))
	depends_on("py-torchvision", type=("build", "run"))
	depends_on("py-torchaudio", type=("build", "run"))
	depends_on("py-typing-extensions", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-setuptools", type="build")
