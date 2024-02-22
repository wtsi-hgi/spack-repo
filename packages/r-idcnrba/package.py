# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdcnrba(RPackage):
	"""Interactive Application for Analyzing Representativeness and
Nonresponse Bias

	Provides access to the 
    Idea Data Center (IDC) application for conducting 
    nonresponse bias analysis (NRBA). The IDC NRBA app is an
    interactive, browser-based Shiny application that can be used to 
    analyze survey data with respect to response rates,
    representativeness, and nonresponse bias. This app provides a user-friendly
    interface to statistical methods implemented by the 'nrba' package.
    Krenzke, Van de Kerckhove, and Mohadjer (2005) 
    <http://www.asasrms.org/Proceedings/y2005/files/JSM2005-000572.pdf>
    and Lohr and Riddles (2016) 
    <https://www150.statcan.gc.ca/n1/en/pub/12-001-x/2016002/article/14677-eng.pdf?st=q7PyNsGR>
    provide an overview of the statistical methods implemented in the application.
	"""
	
	cran = "idcnrba" 

	version("1.1.0", md5="91dda1a9b1819f6aa075128fbbc38556")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-nrba@0.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-flexdashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dt@0.28:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-survey@4.1.1:", type=("build", "run"))
	depends_on("r-srvyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
