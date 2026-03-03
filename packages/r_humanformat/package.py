# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumanformat(RPackage):
	"""Human-Friendly Formatting Functions

	Format quantities of time or bytes into human-friendly strings.
	"""
	
	homepage = "https://github.com/dustin/humanFormat"
	cran = "humanFormat" 

	version("1.2", md5="999c42cc9203f4ecd28d36ffd8109dab")

	depends_on("r-testthat", type=("build", "run"))
