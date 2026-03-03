# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMacer(RPackage):
	"""Molecular Acquisition, Cleaning, and Evaluation in R 'MACER'

	To assist biological researchers in assembling taxonomically and marker focused molecular sequence data sets. 'MACER' accepts a list of genera as a user input and uses NCBI-GenBank and BOLD as resources to download and assemble molecular sequence datasets. These datasets are then assembled by marker, aligned, trimmed, and cleaned. The use of this package allows the publication of specific parameters to ensure reproducibility. The 'MACER' package has four core functions and an example run through using all of these functions can be found in the associated repository <https://github.com/rgyoung6/MACER_example>.
	"""
	
	homepage = "<https://github.com/rgyoung6/MACER>"
	cran = "MACER" 

	version("0.2.1", md5="dfd45a4f8fed9c5d3c361ff6eadc3745")

	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
