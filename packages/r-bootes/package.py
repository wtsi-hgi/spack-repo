# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootes(RPackage):
	"""Bootstrap Confidence Intervals on Effect Sizes

	Calculate robust measures of effect sizes using the bootstrap.
	"""
	
	homepage = "https://github.com/dgerlanc/bootES"
	cran = "bootES" 

	version("1.3.0", md5="caf90c857509d91e1b1b4d6c0dd0c5a6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
