# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphpaf(RPackage):
	"""Estimating and Displaying Population Attributable Fractions

	Estimation and display of various types of population attributable fraction and impact fractions.  As well as the usual calculations of attributable fractions and impact fractions, functions are provided for attributable fraction nomograms and fan plots, continuous exposures, for pathway specific population attributable fractions, and for joint, average and sequential population attributable fractions. 
	"""
	
	homepage = "https://github.com/johnfergusonNUIG/graphPAF"
	cran = "graphPAF" 

	version("2.0.0", md5="3aed5b801e04695336178606d060e8d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-madness", type=("build", "run"))
