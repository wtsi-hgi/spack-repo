# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcts(RPackage):
	"""Clustering Time Series While Resisting Outliers

	Robust Clustering of Time Series (RCTS) has the functionality to cluster time series using both the classical and the robust interactive fixed effects framework. 
  The classical framework is developed in Ando & Bai (2017) <doi:10.1080/01621459.2016.1195743>. The implementation within this package excludes the SCAD-penalty on the estimations of beta. 
  This robust framework is developed in Boudt & Heyndels (2022) <doi:10.1016/j.ecosta.2022.01.002> and is made robust against different kinds of outliers.
  The algorithm iteratively updates beta (the coefficients of the observable variables), group membership, and the latent factors (which can be common and/or group-specific) along
  with their loadings. The number of groups and factors can be estimated if they are unknown.
	"""
	
	cran = "RCTS" 

	version("0.2.4", md5="db48c66ea4ea8d2f3480c49b9228ac00")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-cellwise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
