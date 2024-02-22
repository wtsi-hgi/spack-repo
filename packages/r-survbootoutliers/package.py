# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvbootoutliers(RPackage):
	"""Concordance Based Bootstrap Methods for Outlier Detection in
Survival Analysis

	Three new methods to perform outlier detection in a survival context. In total there are six methods provided, the first three methods are traditional residual-based outlier detection methods, the second three are the concordance-based. Package developed during the work on the two following publications: Pinto J., Carvalho A. and Vinga S. (2015) <doi:10.5220/0005225300750082>; Pinto J.D., Carvalho A.M., Vinga S. (2015) <doi:10.1007/978-3-319-27926-8_22>.
	"""
	
	homepage = "https://github.com/jonydog/survBootOutliers"
	cran = "survBootOutliers" 

	version("1.0", md5="1c072285d101efd54bd223fa7f80e9a6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
