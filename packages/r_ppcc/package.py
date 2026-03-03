# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpcc(RPackage):
	"""Probability Plot Correlation Coefficient Test

	Calculates the Probability Plot Correlation Coefficient (PPCC) 
             between a continuous variable X and a specified distribution. The corresponding 
	     composite hypothesis test that was first introduced by 
	     Filliben (1975) <doi: 10.1080/00401706.1975.10489279> 
	     can be performed to test whether the sample 
	     X is element of either the Normal, log-Normal, Exponential,
	     Uniform, Cauchy, Logistic, Generalized Logistic, Gumbel (GEVI), Weibull,
	     Generalized Extreme Value, Pearson III (Gamma 2), Mielke's Kappa, Rayleigh
	     or Generalized Logistic Distribution. The PPCC test is performed with
	     a fast Monte-Carlo simulation.
	"""
	
	cran = "ppcc" 

	version("1.2", md5="0d0c6be73e7f424997d853c80fb00571")

	depends_on("r@3:", type=("build", "run"))
