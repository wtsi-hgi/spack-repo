# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKdensity(RPackage):
	"""Kernel Density Estimation with Parametric Starts and Asymmetric
Kernels

	Handles univariate non-parametric density estimation with 
    parametric starts and asymmetric kernels in a simple and flexible way. 
    Kernel density estimation with parametric starts involves fitting a
    parametric density to the data before making a correction with kernel 
    density estimation, see Hjort & Glad (1995) <doi:10.1214/aos/1176324627>.
    Asymmetric kernels make kernel density estimation more efficient on bounded
    intervals such as (0, 1) and the positive half-line. Supported asymmetric 
    kernels are the gamma kernel of Chen (2000) <doi:10.1023/A:1004165218295>,
    the beta kernel of Chen (1999) <doi:10.1016/S0167-9473(99)00010-9>, and the
    copula kernel of Jones & Henderson (2007) <doi:10.1093/biomet/asm068>.
    User-supplied kernels, parametric starts, and bandwidths are supported.
	"""
	
	homepage = "https://github.com/JonasMoss/kdensity"
	cran = "kdensity" 

	version("1.1.0", md5="1941e8d3e1663cfed56aad1ed2b711c0")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-univariateml", type=("build", "run"))
	depends_on("r-eql", type=("build", "run"))
