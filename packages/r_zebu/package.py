# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebu(RPackage):
	"""Local Association Measures

	Implements the estimation of local (and global) association measures: Lewontin's D, Ducher's Z, pointwise mutual information, normalized pointwise mutual information and chi-squared residuals. The significance of local (and global) association is accessed using p-values estimated by permutations.
	"""
	
	homepage = "https://github.com/oliviermfmartin/zebu"
	cran = "zebu" 

	version("0.2.2.0", md5="028e130a4d7c37e89f88b0380d2a9f59")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
