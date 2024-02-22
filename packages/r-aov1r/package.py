# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAov1r(RPackage):
	"""Inference in the Balanced One-Way ANOVA Model with Random Factor

	Provides functions to perform statistical inference in the balanced one-way ANOVA model with a random factor: confidence intervals, prediction interval, and Weerahandi generalized pivotal quantities. References: Burdick & Graybill (1992, ISBN-13: 978-0824786441); Weerahandi (1995) <doi:10.1007/978-1-4612-0825-9>; Lin & Liao (2008) <doi:10.1016/j.jspi.2008.01.001>.
	"""
	
	cran = "AOV1R" 

	version("0.1.0", md5="dafd0a5c30c20532f4cb8877871d8afc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cellranger", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
