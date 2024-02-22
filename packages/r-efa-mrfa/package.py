# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfaMrfa(RPackage):
	"""Dimensionality Assessment Using Minimum Rank Factor Analysis

	Performs parallel analysis (Timmerman & Lorenzo-Seva, 2011 
    <doi:10.1037/a0023353>) and hull method (Lorenzo-Seva, Timmerman, & Kiers, 
    2011 <doi:10.1080/00273171.2011.564527>) for assessing the dimensionality
    of a set of variables using minimum rank factor analysis (see ten Berge & 
    Kiers, 1991 <doi:10.1007/BF02294464> for more information). The package 
    also includes the option to compute minimum rank factor analysis by 
    itself, as well as the greater lower bound calculation.
	"""
	
	cran = "EFA.MRFA" 

	version("1.1.2", md5="c462a7b163d0adce55c5793e1a974734")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-pcovr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
