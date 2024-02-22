# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircoutlier(RPackage):
	"""Detection of Outliers in Circular-Circular Regression

	Detection of outliers in circular-circular regression models, modifying its and estimating of models parameters.
	"""
	
	cran = "CircOutlier" 

	version("3.2.3", md5="759f77496ab5479c537ae01214d77160")

	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
