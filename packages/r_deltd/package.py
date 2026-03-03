# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeltd(RPackage):
	"""Kernel Density Estimation using Lifetime Distributions

	A collection of asymmetrical kernels belong to lifetime distributions for kernel density estimation is presented. 
    Mean Squared Errors (MSE) are calculated for estimated curves. For this purpose, R functions allow the distribution to be Gamma, Exponential or Weibull.
    For details see Chen (2000a,b), Jin and Kawczak (2003) and Salha et al. (2014) <doi:10.12988/pms.2014.4616>. 
	"""
	
	homepage = "https://CRAN.R-project.org/package=DELTD"
	cran = "DELTD" 

	version("2.6.8", md5="7ec87f46a27e195bc1cdd15ac319a42b")

	depends_on("r@2.10:", type=("build", "run"))
