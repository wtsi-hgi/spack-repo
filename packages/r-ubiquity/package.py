# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUbiquity(RPackage):
	"""PKPD, PBPK, and Systems Pharmacology Modeling Tools

	Complete work flow for the analysis of pharmacokinetic pharmacodynamic (PKPD), physiologically-based pharmacokinetic (PBPK) and systems pharmacology models including: creation of ordinary differential equation-based models, pooled parameter estimation, individual/population based simulations, rule-based simulations for clinical trial design and modeling assays, deployment with a customizable 'Shiny' app, and non-compartmental analysis. System-specific analysis templates can be generated and each element includes integrated reporting with 'PowerPoint' and 'Word'. 
	"""
	
	homepage = "https://ubiquity.tools/rworkflow"
	cran = "ubiquity" 

	version("2.0.3", md5="7996bf45cab8da9b9bad09e802b7ab74")
	version("2.0.1", md5="002c26dc68ba30f972f2001556ba681d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-onbrand@1.0.2:", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-pknca", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
