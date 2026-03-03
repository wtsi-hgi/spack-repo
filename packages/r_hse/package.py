# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHse(RPackage):
	"""The hse Distribution

	Deprecated.
	"""
	
	cran = "hse" 

	version("0.0-28", md5="8f95368c8f0a6bd838fcfb1773b3cf0f")

	depends_on("r@3.2.2:", type=("build", "run"))
