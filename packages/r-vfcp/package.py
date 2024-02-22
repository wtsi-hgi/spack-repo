# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVfcp(RPackage):
	"""Computation of v Values for U and Copula C(U, v)

	Computation the value of one of two uniformly 
    distributed marginals if the copula probability value is known
    and the value of the second marginal is also known.
    Computation and plotting corresponding cumulative
    distribution function or survival function.
    The numerical definition of a common area limited by lines
    of the cumulative distribution function and survival function.
    Approximate quantification of the probability of this area.
    In addition to 'amh', the copula dimension may be larger than 2.
	"""
	
	cran = "vfcp" 

	version("1.4.0", md5="5a187fee9b6b1cb4b5c43b32dc10f7f9")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
