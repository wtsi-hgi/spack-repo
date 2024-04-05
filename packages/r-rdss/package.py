# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdss(RPackage):
	"""Companion Datasets and Functions for Research Design in the
Social Sciences

	Helper functions to accompany the Blair, Coppock, and Humphreys (2022) "Research Design in the Social Sciences: Declaration, Diagnosis, and Redesign" <https://book.declaredesign.org>. 'rdss' includes datasets, helper functions, and plotting components to enable use and replication of the book. 
	"""
	
	cran = "rdss" 

	version("1.0.6", md5="099bc7785d8616f74690ec89a06ad2f4")
	version("1.0.10", md5="ab89bb5f9cb8a5a0c1892cec33b10799")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dataverse", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-marginaleffects", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-randomizr", type=("build", "run"))
