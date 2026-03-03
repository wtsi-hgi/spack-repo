# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpbstat(RPackage):
	"""Comprehensive Statistical Analysis of Plant Breeding Experiments

	Performs statistical data analysis of various Plant Breeding experiments. Contains functions for Line by Tester analysis as per Arunachalam, V.(1974) <http://repository.ias.ac.in/89299/> and Diallel analysis as per Griffing, B. (1956) <https://www.publish.csiro.au/bi/pdf/BI9560463>.  
	"""
	
	homepage = "https://github.com/nandp1/gpbStat/"
	cran = "gpbStat" 

	version("0.4.3", md5="0f353adb06f926b5eeed32aff83cec48")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
