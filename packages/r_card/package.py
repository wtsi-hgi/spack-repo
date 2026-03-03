# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCard(RPackage):
	"""Cardiovascular and Autonomic Research Design

	Tools that can aid in the assessment of the autonomic regulation 
		of cardiovascular physiology. The aims of this package are to: 1) study 
		electrocardiography (both intervals and morphology) as extensions 
		of signal processing, 2) study circadian rhythms and how it effects 
		autonomic physiology, 3) assess clinical risk of autonomic dysfunction on 
		cardiovascular health through the perspective of epidemiology and causality.
		The analysis of circadian rhythms through cosinor analysis are built upon 
		the methods by Cornelissen (2014) <doi:10.1186/1742-4682-11-16> and 
		Refinetti, Cornelissen, Halberg (2014) <doi:10.1080/09291010600903692>.
	"""
	
	homepage = "https://github.com/asshah4/card"
	cran = "card" 

	version("0.1.0", md5="d73fa2e36ddd2879b2bcc73939aeaace")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-lutz", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
