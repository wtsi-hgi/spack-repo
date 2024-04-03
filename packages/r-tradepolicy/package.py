# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTradepolicy(RPackage):
	"""Replication of 'An Advanced Guide To Trade Policy Analysis'

	Datasets from Yotov, et al. (2016, ISBN:978-92-870-4367-2) "An
    Advanced Guide to Trade Policy Analysis" and functions to report regression
    summaries with clustered robust standard errors.
	"""
	
	homepage = "https://github.com/pachadotdev/tradepolicy/"
	cran = "tradepolicy" 

	version("0.7.0", md5="e8002d8dee39d461bb02c30da26caf83")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-fixest@0.10.4:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
