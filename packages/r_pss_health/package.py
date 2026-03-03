# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPssHealth(RPackage):
	"""Power and Sample Size for Health Researchers via Shiny

	Power and Sample Size for Health Researchers is a Shiny application that brings together a 
    series of functions  related to sample size and power calculations for common analysis in the healthcare 
    field. There are functionalities to calculate the power, sample size to estimate or test hypotheses for means and 
    proportions (including test for correlated groups, equivalence, non-inferiority and superiority), association, correlations coefficients, 
    regression coefficients (linear, logistic, gamma, and Cox), linear mixed model, 
    Cronbach's alpha, interobserver agreement, intraclass correlation coefficients,
    limit of agreement on Bland-Altman plots,
    area under the curve, sensitivity and specificity incorporating the prevalence of disease. 
    You can also use the online version at <https://hcpa-unidade-bioestatistica.shinyapps.io/PSS_Health/>.
	"""
	
	homepage = "https://hcpa-unidade-bioestatistica.shinyapps.io/PSS_Health/"
	cran = "PSS.Health" 

	version("1.0.2", md5="2347571d8453e0c5b6537ae774fae885")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-easypower", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-icc-sample-size", type=("build", "run"))
	depends_on("r-kappasize", type=("build", "run"))
	depends_on("r-longpower", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-powermediation", type=("build", "run"))
	depends_on("r-powersurvepi", type=("build", "run"))
	depends_on("r-presize", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-pwr2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyfeedback", type=("build", "run"))
	depends_on("r-shinyhelper", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
