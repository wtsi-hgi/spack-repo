# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPp(RPackage):
	"""Person Parameter Estimation

	The PP package includes estimation of (MLE, WLE, MAP, EAP, ROBUST)
    person parameters for the 1,2,3,4-PL model and the GPCM (generalized
    partial credit model). The parameters are estimated under the assumption
    that the item parameters are known and fixed. The package is useful e.g. in
    the case that items from an item pool / item bank with known item parameters
    are administered to a new population of test-takers and an ability
    estimation for every test-taker is needed.
	"""
	
	homepage = "https://github.com/jansteinfeld/PP"
	cran = "PP" 

	version("0.6.3-11", md5="c8868750296188fa692a1c2e0ad8ee4f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
