# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugdemand(RPackage):
	"""Drug Demand Forecasting

	Performs drug demand forecasting by modeling drug dispensing data while taking into account predicted enrollment and treatment discontinuation dates. The gap time between randomization and the first drug dispensing visit is modeled using interval-censored exponential, Weibull, log-logistic, or log-normal distributions (Anderson-Bergman (2017) <doi:10.18637/jss.v081.i12>). The number of skipped visits is modeled using Poisson, zero-inflated Poisson, or negative binomial distributions (Zeileis, Kleiber & Jackman (2008) <doi:10.18637/jss.v027.i08>). The gap time between two consecutive drug dispensing visits given the number of skipped visits is modeled using linear regression based on least squares or least absolute deviations (Birkes & Dodge (1993, ISBN:0-471-56881-3)). The number of dispensed doses is modeled using linear or linear mixed-effects models (McCulloch & Searle (2001, ISBN:0-471-19364-X)).
	"""
	
	cran = "drugDemand" 

	version("0.1.2", md5="2a4261e0c42961c7ba42a11a2d45de93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-plotly@4.10.1:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-erify@0.4:", type=("build", "run"))
	depends_on("r-icenreg@2.0.15:", type=("build", "run"))
	depends_on("r-pscl@1.5.5:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
	depends_on("r-nlme@3.1.153:", type=("build", "run"))
	depends_on("r-l1pack@0.41.24:", type=("build", "run"))
	depends_on("r-eventpred@0.2.3:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-dorng@1.8.6:", type=("build", "run"))
	depends_on("r-tictoc@1.1:", type=("build", "run"))
