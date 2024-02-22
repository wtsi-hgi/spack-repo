# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffdfs(RPackage):
	"""Compute the Difference Between Data Frames

	Shows you which rows have changed between two data frames with the same column structure. Useful for diffing slowly mutating data.
	"""
	
	cran = "diffdfs" 

	version("0.9.0", md5="fd87eda4a3521d6a740498031534b670")

	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
