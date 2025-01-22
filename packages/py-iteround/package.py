# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIteround(PythonPackage):
	"""Rounds iterables (arrays, lists, sets, etc) while maintaining the sum of the initial array."""
	
	homepage = "https://github.com/cgdeboer/iteround"
	pypi = "iteround/iteround-1.0.4-py3-none-any.whl" 

	version("1.0.0", sha256="5b9ebd93edfda0f14d075863e55d8e10383984e942575bf87d7a48b958fe18b7", expand=False, url="https://files.pythonhosted.org/packages/ab/d9/2ab3a5347710d05c535276bc3ec44c5a6c7042d8b543bf75a719b920b532/iteround-1.0.0-py3-none-any.whl")
	version("1.0.2", sha256="b280fe1b52818a5741ab6d6814ccba8b62ea8758acecb11765d8d77eb29a75fe", expand=False, url="https://files.pythonhosted.org/packages/35/1d/ad1084701aa0e259a4e7f343ec32c94b2c799c377dadb2326133065275c9/iteround-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="5392c0bc2b7f713b01c709b89485356104db48235ffdd84580ce999d4c8fbfb8", expand=False, url="https://files.pythonhosted.org/packages/a6/2e/d8005b97a8cecd0adab8ccc362b8794eae9a7f07ab5cdaa7ac2e24dfccff/iteround-1.0.3-py3-none-any.whl")
	version("1.0.4", sha256="17947dd5479177e6fb186b0a3d5d594b55eedea14dc722c6da7e84bbed45f5b2", expand=False, url="https://files.pythonhosted.org/packages/26/c7/68d920f791cd99919d82dd6db9fc0aca3790dc8d67c69b559a447ca2a914/iteround-1.0.4-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
