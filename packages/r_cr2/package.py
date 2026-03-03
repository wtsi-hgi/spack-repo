# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCr2(RPackage):
	"""Compute Cluster Robust Standard Errors with Degrees of Freedom
Adjustments

	Estimate different types of cluster robust standard errors (CR0, CR1, CR2) with degrees of freedom adjustments. Standard errors are computed based on 'Liang and Zeger' (1986) <doi:10.1093/biomet/73.1.13> and Bell and 'McCaffrey' <https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2002002/article/9058-eng.pdf?st=NxMjN1YZ>. Functions used in Huang and Li <doi:10.3758/s13428-021-01627-0>, Huang, 'Wiedermann', and 'Zhang' <doi:10.1080/00273171.2022.2077290>, and Huang, 'Zhang', and Li (forthcoming: Journal of Research on Educational Effectiveness).
	"""
	
	homepage = "https://github.com/flh3/CR2"
	cran = "CR2" 

	version("0.2.1", md5="a918360d9ac1b236929e564361afa98d", url="https://cran.r-project.org/src/contrib/CR2_0.2.1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
