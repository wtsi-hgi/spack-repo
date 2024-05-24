# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVaexViz(PythonPackage):
	"""Visualization for vaex"""
	
	homepage = "https://www.github.com/maartenbreddels/vaex"
	pypi = "vaex-viz/vaex_viz-0.5.4-py3-none-any.whl" 

	version("0.1.0", sha256="b4641b826e2c9f4de3c13b15dd2c362d88c981aeab210e19e53d57f94a70ed6d")
	version("0.1.1", sha256="4ae0fcfdc005abfb7be929e0c7f1bb5a99931cc8a8557cb0c36c485ebc23b5a2")
	version("0.1.2", sha256="624323de6586250432de649be84d3038a2923edbe961151e1b0c705bfd9ad1dd")
	version("0.1.3", sha256="fd3b8a641076f2fb67e8b634e4489484464462c40c210dcbc96b402aae2ae8cb")
	version("0.2.0", sha256="ff1889d0651f4d58795949f7127ab59e16fece9f943005a2986f8ede7e741c8c")
	version("0.2.1", sha256="ff0b36a38baeeedb1d2a88ba7fe2939446aea0b7346d8b5aa8f7d658f19fbf97")
	version("0.2.2", sha256="cdae4a8627ed51c0f8cff7b0ed5e17988789e6ed2c52e9d96b5cc83cf23ad0a6")
	version("0.3.0", sha256="4798184f51f171405c9252dd1fa6baa71ade0a0d019a9df795cc48fc8e50181a")
	version("0.3.1", sha256="d1e9ab6daec0d4cf81d97cf991c42333aebd231bd0c273988dcb40b2bdf6a322")
	version("0.3.2", sha256="7e2c4f040af0666d6642de365762783e7d6a6066c52e6dc53f575b7556476030")
	version("0.3.3", sha256="b6e1070741a1afbb9a4d6be31eb1569a72d42e69cecf3113d3452adc0479c99f")
	version("0.3.4", sha256="5cfd100662f1aa975b4e710e97053996c6fee77c85e8a0f92f2bc155c834625c")
	version("0.3.5", sha256="894171c91721c4e87e612e0dc54e9079e944160b3eadaf2bd1f19aaf14ed1bf5")
	version("0.3.6", sha256="6622901a8b3d64c5fe3c29b16d35442e71da55963a79a4e62c9f9f3ab119d746")
	version("0.3.7", sha256="69d3b0a23dc9f13fcd4d99afda100fefe0962e606a79de47c3b6f1d39511cf6f")
	version("0.3.8", sha256="2d14252e0ba46a123dc47dd151fdca737a46afaef7ee642456320d9ccde67077")
	version("0.4.0", sha256="2d177b2afc7f15711cd2ef40ba21cf7f48c20c23af6f909a5ca2763dca8dedc6", expand=False, url="https://files.pythonhosted.org/packages/ee/9f/abaf285f1a6ef1a3bfc3d65d3ef292e6b253d6a50555950227bff0ddb04a/vaex_viz-0.4.0-py3-none-any.whl")
	version("0.4.0a1", sha256="e1db275816a3f62723c9903e4a8a34e46df6cc1301acf8dbf6977ba14ec7cb30")
	version("0.5.0", sha256="03b728c6bb1a000e10455862623eba8639f844e218869e370c5cdd87867d43a2", expand=False, url="https://files.pythonhosted.org/packages/9e/b0/a1855b9cade638315ce0f82763d8800f19335487e59acee6cc8a1c350b3c/vaex_viz-0.5.0-py3-none-any.whl")
	version("0.5.0.dev1", sha256="f33743e52522ac035be43f8f86c9c17aef289984fffd2a36bece010e304466e4", expand=False, url="https://files.pythonhosted.org/packages/a8/84/ebb21fdd741eb22f68ce1616093af599b503f3bf9efe449bb0aea55a4bf4/vaex_viz-0.5.0.dev1-py3-none-any.whl")
	version("0.5.1", sha256="0c539b8729dcf2aad656da9fc6d0954d0151c1a4fc56491121a8b8a1c6712f12", expand=False, url="https://files.pythonhosted.org/packages/35/af/7642b4fe4dceef9f13f5172872cb81c891efd9c4b22c4f1373044849156d/vaex_viz-0.5.1-py3-none-any.whl")
	version("0.5.2", sha256="f52097f539d5d17c27c0e2b2a6ef69f65addc16702bb0c53085a0b0215d3afa1", expand=False, url="https://files.pythonhosted.org/packages/e7/db/5b16e8a334ec0479be535db9b4af5ebef7916486a3dd9daee2678f0d7244/vaex_viz-0.5.2-py3-none-any.whl")
	version("0.5.3", sha256="7d1bc48f3076a3edc39af28dfe363103d86b8893dda68ee1d19f30d4069ee7c6", expand=False, url="https://files.pythonhosted.org/packages/ec/05/5c26b3d84898a65a165fed099e14185f5678a4b8c444177ee586fdefa39b/vaex_viz-0.5.3-py3-none-any.whl")
	version("0.5.4", sha256="7e8d0cc06ac47e8d00cdb2ac2ea679218afe72200234675f3c9645bbbcf53f40", expand=False, url="https://files.pythonhosted.org/packages/8c/e9/e96b5527a85c7deda12d438a33f2ec2cf6ce0aa397906b3469133c1184a6/vaex_viz-0.5.4-py3-none-any.whl")

	depends_on("py-pillow", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-vaex-core", type=("build", "run"))
