# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTraittypes(PythonPackage):
	"""Scipy trait types"""
	
	homepage = "http://ipython.org"
	pypi = "traittypes/traittypes-0.2.1-py2.py3-none-any.whl" 

	version("0.0.1", sha256="16ca7748f1cb4589f5fba4dc45b99280d61238d4a4370e5ef10855013cb79ec8", expand=False, url="https://files.pythonhosted.org/packages/ed/70/1bd7142aecebaf243823842a94cead874d8faf36072a3f5295114db4e05f/traittypes-0.0.1-py2.py3-none-any.whl")
	version("0.0.2", sha256="3587f58d6803bdad421a6696a5c8b519c7efde8b30641f470572bec1b65b825f", expand=False, url="https://files.pythonhosted.org/packages/35/a0/74b53b7f6395d522cd42a03069483484399e93dfa8f25d1620d26e0c3ac4/traittypes-0.0.2-py2.py3-none-any.whl")
	version("0.0.3", sha256="c7edcabaf7c5b9f69cfdd556d03a57e16dd5d42e81541c6cff719163452b6fc0", expand=False, url="https://files.pythonhosted.org/packages/dc/28/766a4fa0960ef2aec1d6bc05a22ccb935a82f6d542448488203797cc8126/traittypes-0.0.3-py2.py3-none-any.whl")
	version("0.0.4", sha256="f8c21014a0090bf221bf7afd2bca9c962e03dcd3ec812521636312f01bc2680c", expand=False, url="https://files.pythonhosted.org/packages/69/0c/bef267c051ccd4a8b7bea9643f71d586426f0121e698893eb6349a369bb5/traittypes-0.0.4-py2.py3-none-any.whl")
	version("0.0.5", sha256="6bdd21a1aec4104208b3a32b8e2f2d76db409da76f7ae062893f9899aa6295ee", expand=False, url="https://files.pythonhosted.org/packages/c9/7c/0e3958a8fa11d081be90a3e5412968250f22c646ca33a2b379deb9e5dcf9/traittypes-0.0.5-py2.py3-none-any.whl")
	version("0.0.6", sha256="f0b17ff1cdeeece9ae706673726c16ab6d0a01ce31b6886e1e17357cd7828b7e", expand=False, url="https://files.pythonhosted.org/packages/96/fe/60620d6411c49f96aed04aaa59240b9fd532f2c552a897f24cdd02089f0a/traittypes-0.0.6-py2.py3-none-any.whl")
	version("0.1.0", sha256="a4f49f4cfdaa00cde45c7f5b457d30d4503b778b9178e1e4b99eebfed3e1f43b", expand=False, url="https://files.pythonhosted.org/packages/73/06/ed815ef101d52e9aa3105580768572c53904cf1e7468867f7194efdcc0ed/traittypes-0.1.0-py2.py3-none-any.whl")
	version("0.2.0", sha256="816b73bbe90764e4e7b235989befd71614a0d7be7662d09029ed86bc04151a0d", expand=False, url="https://files.pythonhosted.org/packages/e5/b7/13f1ae486377c3d7145b0d78f80ad8d80a5cfd8ec05f32eb6e5033496573/traittypes-0.2.0-py2.py3-none-any.whl")
	version("0.2.1", sha256="1340af133810b6eee1a2eb2e988f862b0d12b6c2d16f282aaf3207b782134c2e", expand=False, url="https://files.pythonhosted.org/packages/9c/d1/8d5bd662703cc1764d986f6908a608777305946fa634d34c470cd4a1e729/traittypes-0.2.1-py2.py3-none-any.whl")

	depends_on("py-traitlets", type=("build", "run"))
