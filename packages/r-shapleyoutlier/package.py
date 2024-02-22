# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapleyoutlier(RPackage):
	"""Multivariate Outlier Explanations using Shapley Values and
Mahalanobis Distances

	Based on Shapley values to explain multivariate outlyingness and to detect and impute cellwise outliers.
    Includes implementations of methods described in Mayrhofer and Filzmoser (2022) <doi:10.48550/ARXIV.2210.10063>.
	"""
	
	cran = "ShapleyOutlier" 

	version("0.1.1", md5="88404a26ba0328b55ce004f40e2ffde6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
