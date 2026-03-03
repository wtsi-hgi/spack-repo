# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmboot(RPackage):
	"""Bootstrap in Linear Models

	Various efficient and robust bootstrap methods are implemented for 
    linear models with least squares estimation.  Functions within this package 
    allow users to create bootstrap sampling distributions for model parameters, 
    test hypotheses about parameters, and visualize the bootstrap sampling or null 
    distributions.  Methods implemented for linear models include the wild bootstrap by 
    Wu (1986) <doi:10.1214/aos/1176350142>, the residual and paired bootstraps by
    Efron (1979, ISBN:978-1-4612-4380-9), the delete-1 jackknife by 
    Quenouille (1956) <doi:10.2307/2332914>, and the Bayesian bootstrap by 
    Rubin (1981) <doi:10.1214/aos/1176345338>.
	"""
	
	cran = "lmboot" 

	version("0.0.1", md5="639eac79a3a0de3c7bee8c343606fd76")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-evd@2.3:", type=("build", "run"))
