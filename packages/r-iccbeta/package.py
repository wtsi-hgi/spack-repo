# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIccbeta(RPackage):
	"""Multilevel Model Intraclass Correlation for Slope Heterogeneity

	A function and vignettes for computing an intraclass correlation
    described in Aguinis & Culpepper (2015) <doi:10.1177/1094428114563618>.
    This package quantifies the share of variance in a dependent variable that
    is attributed to group heterogeneity in slopes.
	"""
	
	homepage = "https://github.com/tmsalab/iccbeta"
	cran = "iccbeta" 

	version("1.2.0", md5="31d974d52e33541982615754c6e8b1fc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.200:", type=("build", "run"))
