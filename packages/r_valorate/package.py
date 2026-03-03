# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValorate(RPackage):
	"""Velocity and Accuracy of the LOg-RAnk TEst

	The algorithm implemented in this package was
    designed to quickly estimates the distribution of the 
    log-rank especially for heavy unbalanced groups. VALORATE 
    estimates the null distribution and the p-value of the 
    log-rank test based on a recent formulation. For a given 
    number of alterations that define the size of survival 
    groups, the estimation involves a weighted sum of 
    distributions that are conditional on a co-occurrence term 
    where mutations and events are both present. The estimation 
    of conditional distributions is quite fast allowing the 
    analysis of large datasets in few minutes 
    <http://bioinformatica.mty.itesm.mx/valorate>.
	"""
	
	homepage = "http://bioinformatica.mty.itesm.mx/valorate"
	cran = "valorate" 

	version("1.0-1", md5="267e1a837fca724954d88f901892a7e7")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
