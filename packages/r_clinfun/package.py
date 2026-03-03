# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinfun(RPackage):
	"""Clinical Trial Design and Data Analysis Functions

	Utilities to make your clinical collaborations easier if not
          fun. It contains functions for designing studies such as Simon
          2-stage and group sequential designs and for data analysis such
          as Jonckheere-Terpstra test and estimating survival quantiles.
	"""
	
	cran = "clinfun" 

	version("1.1.5", md5="5af2123784734234a5dcb5eeb4195c2b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
