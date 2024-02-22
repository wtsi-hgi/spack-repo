# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocor(RPackage):
	"""Analyze Isotope Ratios in a 'Shiny'-App

	Analyzing Inductively Coupled Plasma - Mass Spectrometry (ICP-MS) 
    measurement data to evaluate isotope ratios (IRs) is a complex process.
    The 'IsoCor' package facilitates this process and renders it reproducible 
    by providing a function to run a 'Shiny'-App locally in any web browser. 
    In this App the user can upload data files of various formats, select ion 
    traces, apply peak detection and perform calculation of IRs and delta values.
    Results are provided as figures and tables and can be exported.
    The App, therefore, facilitates data processing of ICP-MS experiments to
    quickly obtain optimal processing parameters compared to traditional 'Excel'
    worksheet based approaches. A more detailed description can be found in the
    corresponding article "Data processing made easy: standalone tool for 
    automated calculation of isotope ratio from transient signals – IsoCor" 
    by Tukhmetova et al. in Journal of Analytical Atomic Spectrometry (JAAS).
    The most recent version of 'IsoCor' can be tested online 
    at <https://jali.shinyapps.io/isocor>.
	"""
	
	homepage = "https://jali.shinyapps.io/isocor"
	cran = "IsoCor" 

	version("0.1.40", md5="c4c7bb73c9dbf69b25f03d6031061ad4")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-maldiquant", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyalert", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
