# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsane(RPackage):
	"""INsulin Secretion ANalysEr

	A user-friendly interface, using Shiny, to analyse glucose-stimulated insulin secretion (GSIS) 
    assays in pancreatic beta cells or islets.
    The package allows the user to import several sets of experiments from different spreadsheets 
    and to perform subsequent steps: summarise in a tidy format, visualise data quality 
    and compare experimental conditions without omitting to account for technical confounders 
    such as the date of the experiment or the technician.
    Together, insane is a comprehensive method that optimises pre-processing and analyses of 
    GSIS experiments in a friendly-user interface.
    The Shiny App was initially designed for EndoC-betaH1 cell line following method described 
    in Ndiaye et al., 2017 (<doi:10.1016/j.molmet.2017.03.011>).
	"""
	
	homepage = "https://github.com/mcanouil/insane/"
	cran = "insane" 

	version("1.0.3", md5="483bcce7659af5e67449e5c8d6670de2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-broom@0.5.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-dt@0.13:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-ggpubr@0.3:", type=("build", "run"))
	depends_on("r-glue@1.4.1:", type=("build", "run"))
	depends_on("r-patchwork@1.0.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
