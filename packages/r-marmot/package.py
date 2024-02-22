# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarmot(RPackage):
	"""Matching on Poset-Based Average Rank for Multiple Treatments
(MARMoT)

	It contains the function to apply MARMoT balancing technique discussed in: Silan, Boccuzzo, Arpino (2021) <DOI:10.1002/sim.9192>, Silan, Belloni, Boccuzzo, (2023) <DOI:10.1007/s10260-023-00695-0>; 
             furthermore it contains a function for computing the Deloof's approximation of the average rank 
             (and also a parallelized version) and a function to compute the Absolute Standardized Bias. 
	"""
	
	cran = "MARMoT" 

	version("0.0.4", md5="a11fa9fc9f2559ea99c3d5c6ae4e5501")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-parsec", type=("build", "run"))
