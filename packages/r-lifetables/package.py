# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifetables(RPackage):
	"""Two-Parameter HMD Model Life Table System

	Functions supplied in this package will implement
        discriminant analysis to select an appropriate life table
        family, select an appropriate alpha level based on a desired
        life expectancy at birth, produce a model mortality pattern
        based on family and level as well as plot the results.
	"""
	
	cran = "LifeTables" 

	version("1.0", md5="770f167442938b24908cf4ed2b0a9347")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
