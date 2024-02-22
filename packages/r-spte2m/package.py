# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpte2m(RPackage):
	"""Nonparametric Modeling and Monitoring of Spatio-Temporal Data

	Spatio-temporal data have become increasingly popular in many research fields. Such data often have complex structures that are difficult to describe and estimate. This package provides reliable tools for modeling complicated spatio-temporal data. It also includes tools of online process monitoring to detect possible change-points in a spatio-temporal process over time. More specifically, the package implements the spatio-temporal mean estimation procedure described in Yang and Qiu (2018) <doi:10.1002/sim.7622>, the spatio-temporal covariance estimation procedure discussed in Yang and Qiu (2019) <doi:10.1002/sim.8315>, the three-step method for the joint estimation of spatio-temporal mean and covariance functions suggested by Yang and Qiu (2022) <doi:10.1007/s10463-021-00787-2>, the spatio-temporal disease surveillance method discussed in Qiu and Yang (2021) <doi:10.1002/sim.9150> that can accommodate the covariate effect, the spatial-LASSO-based process monitoring method proposed by Qiu and Yang (2023) <doi:10.1080/00224065.2022.2081104>, and the online spatio-temporal disease surveillance method described in Yang and Qiu (2020) <doi:10.1080/24725854.2019.1696496>.
	"""
	
	cran = "SpTe2M" 

	version("1.0.3", md5="21d5836164b6f52b1487bf891a6a7939")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
