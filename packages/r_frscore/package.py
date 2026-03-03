# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrscore(RPackage):
	"""Functions for Calculating Fit-Robustness of CNA-Solutions

	Functions for automatically performing 
             a reanalysis series
             on a data set using CNA, and for calculating the fit-robustness
             of the resulting models, as described in 
             Parkkinen and Baumgartner (2021) <doi:10.1177/0049124120986200>.
	"""
	
	cran = "frscore" 

	version("0.3.1", md5="dc63eb222e1060f1601c4a4bcd38e26a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cna@3.5.1:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
