# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtdl(RPackage):
	"""The Generalized Time-Dependent Logistic Family

	Computes the  probability density, survival function,
   the hazard rate functions and generates random samples from the 
   GTDL distribution given by Mackenzie, G. (1996) <doi:10.2307/2348408>. 
   The likelihood estimates, the randomized quantile (Louzada, F., et al. 
   (2020) <doi:10.1109/ACCESS.2020.3040525>)
   residuals and the normally transformed randomized survival 
   probability (Li,L., et al. (2021) <doi:10.1002/sim.8852>)
   residuals are obtained for the GTDL model. 
	"""
	
	cran = "GTDL" 

	version("1.0.0", md5="318866678838ca1fb214088e0b4cda20")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
