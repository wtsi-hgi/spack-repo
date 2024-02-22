# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeex(RPackage):
	"""An API for M-Estimation

	Provides a general, flexible framework for estimating parameters
    and empirical sandwich variance estimator from a set of unbiased estimating
    equations (i.e., M-estimation in the vein of Stefanski & Boos (2002)
    <doi:10.1198/000313002753631330>). All examples from Stefanski & Boos (2002)
    are published in the corresponding Journal of Statistical Software paper
    "The Calculus of M-Estimation in R with geex" by Saul & Hudgens (2020)
    <doi:10.18637/jss.v092.i02>. Also provides an API to compute finite-sample 
    variance corrections.
	"""
	
	homepage = "https://github.com/bsaul/geex"
	cran = "geex" 

	version("1.1.1", md5="af6114bbc9e67c59806a879ecea300da")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix@1.2.6:", type=("build", "run"))
	depends_on("r-rootsolve@1.6.6:", type=("build", "run"))
	depends_on("r-numderiv@2014.2.1:", type=("build", "run"))
	depends_on("r-lme4@1.1.12:", type=("build", "run"))
