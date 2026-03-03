# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApc(RPackage):
	"""Age-Period-Cohort Analysis

	Functions for age-period-cohort analysis. Aggregate data can be organised in matrices indexed by age-cohort, age-period or cohort-period. The data can include dose and response or just doses. The statistical model is a generalized linear model (GLM) allowing for 3,2,1 or 0 of the age-period-cohort factors. Individual-level data should have a row for each individual and columns for each of age, period, and cohort. The statistical model for repeated cross-section is a generalized linear model. The statistical model for panel data is ordinary least squares. The canonical parametrisation of Kuang, Nielsen and Nielsen (2008) <DOI:10.1093/biomet/asn026> is used. Thus, the analysis does not rely on ad hoc identification.
	"""
	
	cran = "apc" 

	version("2.0.0", md5="a06d4a3c58ddb620cc9a25540510d6fa")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-islr", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-chainladder", type=("build", "run"))
