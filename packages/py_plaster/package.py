# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPlaster(PythonPackage):
	"""A loader interface around multiple config file formats."""
	
	homepage = "https://docs.pylonsproject.org/projects/plaster/en/latest/"
	pypi = "plaster/plaster-1.1.2-py2.py3-none-any.whl" 

	version("0.1.0", sha256="d56c4e1dc6d17d8e9ffb200cb0e10e6c86af70f4dd565ce808f895987096ca09", expand=False, url="https://files.pythonhosted.org/packages/08/9b/b429c80369020513ae34f5c2f76518c495c768d9afad1dfb88ee4e517640/plaster-0.1.0-py2.py3-none-any.whl")
	version("0.2", sha256="98df254083b92d491e9d7423290359e52d636eff62ce5917e12bf8bfa898e153", expand=False, url="https://files.pythonhosted.org/packages/91/a0/8ea1ecf1c169d6430dfe63dff20d64fd1b9d655496cd8b67376eab459c5a/plaster-0.2-py2.py3-none-any.whl")
	version("0.3", sha256="79a1cf7324c7802c1f3fd643cde93b62a3a210cc20f99f89920fe71a9956f08a", expand=False, url="https://files.pythonhosted.org/packages/43/63/2148a3052ac9762b33972ddf6b836df0499262c1c9a13c33b9af1816430e/plaster-0.3-py2.py3-none-any.whl")
	version("0.4", sha256="4f419205c585105dd9c008aee8686086b4a29405a6ae89cd0674cdd350ca8b8c", expand=False, url="https://files.pythonhosted.org/packages/84/b3/2a425cf9eacc000f501ae5a1e7e397f097807004c70da7e395896c161054/plaster-0.4-py2.py3-none-any.whl")
	version("0.5", sha256="626f4c2ffaaa101b9eced20da42fe44c460f1b0bb52b0add37b4836516978f53", expand=False, url="https://files.pythonhosted.org/packages/49/4c/7a110fe39ed78f3ccbe1ebb94da450bb23423f3fe8d5c6e16bb5c47ff95f/plaster-0.5-py2.py3-none-any.whl")
	version("1.0", sha256="215c921a438b5349931fd7df9a5a11a3572947f20f4bc6dd622ac08f1c3ba249", expand=False, url="https://files.pythonhosted.org/packages/61/29/3ac8a5d03b2d9e6b876385066676472ba4acf93677acfc7360b035503d49/plaster-1.0-py2.py3-none-any.whl")
	version("1.1", sha256="50a76cfa6a283f712660110fb82e254f5444b99a2df5837426eea0b8b47bbd5e", expand=False, url="https://files.pythonhosted.org/packages/81/ed/6a029285fc7eeb76e19e334a79558c751e95eb1fcb60bfbc261e2f5e8356/plaster-1.1-py2.py3-none-any.whl")
	version("1.1.1", sha256="4eaa4358001b7cd7bc6346550fdef6a935bce870a1296f4e78e75cadc391e9d4", expand=False, url="https://files.pythonhosted.org/packages/7b/59/d304cdcb2638da23e3ade4a59abc7ce6d9e8b914776b615fb0c744ec911c/plaster-1.1.1-py2.py3-none-any.whl")
	version("1.1.2", sha256="42992ab1f4865f1278e2ad740e8ad145683bb4022e03534265528f0c23c0df2d", expand=False, url="https://files.pythonhosted.org/packages/e7/8b/3f98db1448e3b4d2d142716874a7e02f6101685fdaa0f55a8668e9ffa048/plaster-1.1.2-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.7:", type=("build", "run"))

# {'setuptools': ['0.1.0', '0.2', '0.3', '0.4', '0.5', '1.0'], "Sphinx;extra=='docs'": ['0.1.0', '0.2', '0.3', '0.4', '0.5', '1.0', '1.1', '1.1.1', '1.1.2'], "pylons-sphinx-themes;extra=='docs'": ['0.1.0', '0.2', '0.3', '0.4', '0.5', '1.0', '1.1', '1.1.1', '1.1.2'], "mock;extra=='testing'": ['0.1.0', '0.2'], "pytest;extra=='testing'": ['0.1.0', '0.2', '0.3', '0.4', '0.5', '1.0', '1.1', '1.1.1', '1.1.2'], "pytest-cov;extra=='testing'": ['0.1.0', '0.2', '0.3', '0.4', '0.5', '1.0', '1.1', '1.1.1', '1.1.2'], 'importlib-metadata;python_version<"3.8"': ['1.1', '1.1.1', '1.1.2']}