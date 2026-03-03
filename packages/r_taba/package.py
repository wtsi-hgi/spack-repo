# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaba(RPackage):
	"""Taba Robust Correlations

	Calculates the robust Taba linear, Taba rank (monotonic), TabWil, and TabWil rank 
    correlations. Test statistics as well as one sided or two sided p-values are provided 
    for all correlations. Multiple correlations and p-values can be calculated 
    simultaneously across multiple variables. In addition, users will have the option to use 
    the partial, semipartial, and generalized partial correlations; where the partial and 
    semipartial correlations use linear, logistic, or Poisson regression to modify the specified
    variable. 
	"""
	
	cran = "Taba" 

	version("1.0.0", md5="407ad00f05bb04df99fffe5f2d4cb578")

	depends_on("r-robustbase", type=("build", "run"))
