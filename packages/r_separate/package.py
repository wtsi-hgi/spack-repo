# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeparate(RPackage):
	"""Maximum Likelihood Estimation and Likelihood Ratio Test
Functions for Separable Variance-Covariance Structures

	Maximum likelihood estimation of the parameters
    of matrix and 3rd-order tensor normal distributions with unstructured
    factor variance covariance matrices, two procedures, and for unbiased
    modified likelihood ratio testing of simple and double separability
    for variance-covariance structures, two procedures. References:
    Dutilleul P. (1999) <doi:10.1080/00949659908811970>, 
    Manceur AM, Dutilleul P. (2013)
    <doi:10.1016/j.cam.2012.09.017>, and Manceur AM, Dutilleul 
    P. (2013) <doi:10.1016/j.spl.2012.10.020>.
	"""
	
	cran = "sEparaTe" 

	version("0.3.2", md5="4a86d8cb4446cabb38dbfac4fcf20b19")

	depends_on("r@4.3:", type=("build", "run"))
