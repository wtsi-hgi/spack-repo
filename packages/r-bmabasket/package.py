# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmabasket(RPackage):
	"""Bayesian Model Averaging for Basket Trials

	An implementation of the Bayesian model averaging method 
    of Psioda and others (2019) <doi:10.1093/biostatistics/kxz014> for basket trials. 
    Contains a user-friendly wrapper for simulating basket trials under conditions 
    and analyzing them with a Bayesian model averaging approach.
	"""
	
	homepage = "https://github.com/ethan-alt/bmabasket"
	cran = "bmabasket" 

	version("0.1.2", md5="1ed60918b831a3671083b10725214f87")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
