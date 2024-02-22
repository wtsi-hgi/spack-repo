# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabolic(RPackage):
	"""Datasets and Functions for Reproducing Meta-Analyses

	Dataset and functions from the meta-analysis published in Medicine & Science in Sports & Exercise. 
    It contains all the data and functions to reproduce the analysis.
    "Effectiveness of HIIE versus MICT in Improving Cardiometabolic Risk Factors in Health and Disease: A Meta-analysis".
    Felipe Mattioni Maturana, Peter Martus, Stephan Zipfel, Andreas M Nieß (2020) <doi:10.1249/MSS.0000000000002506>.
	"""
	
	homepage = "https://github.com/fmmattioni/metabolic"
	cran = "metabolic" 

	version("0.1.2", md5="23e1d8b05feb61c9a61db7406ec6dbe9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-ggfittext", type=("build", "run"))
	depends_on("r-cli@2.0.1:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggimage", type=("build", "run"))
	depends_on("r-patchwork@1:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-meta@4.11.0:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
