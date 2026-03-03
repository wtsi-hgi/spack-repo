# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPafr(RPackage):
	"""Read, Manipulate and Visualize 'Pairwise mApping Format' Data

	Provides functions to read, process and visualize pairwise sequence 
 alignments in the 'PAF' format used by 'minimap2' and other whole-genome aligners. 
 'minimap2' is described by Li H. (2018) <doi:10.1093/bioinformatics/bty191>.
	"""
	
	homepage = "https://dwinter.github.io/pafr/"
	cran = "pafr" 

	version("0.0.2", md5="bbd2e6b313bb4452fda236f847e9cb81")

	depends_on("r@3.4.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
