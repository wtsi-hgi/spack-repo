# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbanova(RPackage):
	"""Parametric Bootstrap for ANOVA Models

	Parametric bootstrap (PB) has been used for 
             three-way ANOVA model with unequal group variances.
	"""
	
	cran = "pbANOVA" 

	version("0.1.0", md5="0b42e4adcede1afcffbf46bbc7d5f743")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
