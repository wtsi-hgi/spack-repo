# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyYamlordereddictloader(PythonPackage):
	"""YAML loader and dumper for PyYAML allowing to keep keys order."""
	
	homepage = "https://github.com/fmenabe/python-yamlordereddictloader"
	pypi = "yamlordereddictloader/yamlordereddictloader-0.4.2-py3-none-any.whl" 

	version("0.1.0", sha256="2b82d3573077abc9604fe0e34d6f9172687baf6a7033e2f278b498232da234be")
	version("0.1.1", sha256="b4f0d1b6c0d56ce83accef3c228b2eb060d3d5d45238d37365af9268ce4e65ed")
	version("0.2.0", sha256="a03500d797776ce29ce4a10f4974ed25b16a84262155f6a0b418902f42e94697")
	version("0.2.2", sha256="a9153e0f36f2bf6e3d701fbda50d5100e887785a1db6c446b5bd1320ce9eb47f")
	version("0.3.0", sha256="24db7896db4879080c7bb8e1f303bd9fdd3655d8b257077ec9e3f894c2bf9dc5")
	version("0.4.0", sha256="7f30f0b99ea3f877f7cb340c570921fa9d639b7f69cba18be051e27f8de2080e")
	version("0.4.2", sha256="dc048adb67026786cd24119bd71241f35bc8b0fd37d24b415c37bbc8049f9cd7", expand=False, url="https://files.pythonhosted.org/packages/d3/b6/64e84e26c52343dc48e9ffefd7d5e82b986f3bc2bd6da753420f41645718/yamlordereddictloader-0.4.2-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-pyyaml", type=("build", "run"))

# {'pyyaml': ['0.4.2']}