# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnival(RPackage):
	"""Assessing Essential Unidimensionality Using External Validity
Information

	Assess essential unidimensionality using external validity
    information  using the procedure proposed by Ferrando & Lorenzo-Seva
    (2019) <doi:10.1177/0013164418824755>. Provides two indices for assessing
    differential  and incremental validity, both based on a second-order 
    modelling schema for the general factor.
	"""
	
	cran = "unival" 

	version("1.1.0", md5="f026d8d24a134fb56a9f868cceeccd11")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
