# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubh(RPackage):
	"""A Toolbox for Public Health and Epidemiology

	A toolbox for making R functions and capabilities more
    accessible to students and professionals from Epidemiology and
    Public Health related disciplines. Includes a function to report 
    coefficients and confidence intervals from models using robust
    standard errors (when available), functions that expand 'ggplot2'
    plots and functions relevant for introductory papers in Epidemiology 
    or Public Health. Please note that use of the 
    provided data sets is for educational purposes only.
	"""
	
	cran = "pubh" 

	version("1.3.2", md5="f409b8bcd4c1801333f8fb95853fed1c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggformula", type=("build", "run"))
	depends_on("r-gtsummary", type=("build", "run"))
	depends_on("r-huxtable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-epi", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-moonbook", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
