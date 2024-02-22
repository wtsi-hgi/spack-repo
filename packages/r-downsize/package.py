# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDownsize(RPackage):
	"""A Tool to Downsize Large Analysis Projects for Testing

	Toggles the test and production versions of a large
  data analysis project.
	"""
	
	homepage = "https://github.com/wlandau/downsize"
	cran = "downsize" 

	version("0.2.3", md5="6fe2080d2ce201e8abf708210d8568a6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
