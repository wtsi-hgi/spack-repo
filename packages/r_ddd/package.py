# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdd(RPackage):
	"""Diversity-Dependent Diversification

	
 Implements maximum likelihood and bootstrap methods based on
 the diversity-dependent birth-death process to test whether
 speciation or extinction are diversity-dependent, under various
 models including various types of key innovations.
 See Etienne et al. 2012, Proc. Roy. Soc. B 279: 1300-1309,
 <DOI:10.1098/rspb.2011.1439>,
 Etienne & Haegeman 2012, Am. Nat. 180: E75-E89,
 <DOI:10.1086/667574>,
 Etienne et al. 2016. Meth. Ecol. Evol. 7: 1092-1099,
 <DOI:10.1111/2041-210X.12565> and
 Laudanno et al. 2021. Syst. Biol. 70: 389–407,
 <DOI:10.1093/sysbio/syaa048>.
 Also contains functions to simulate the diversity-dependent
 process.
	"""
	
	cran = "DDD" 

	version("5.2.2", md5="b1b296ef0cfdf5d47fd6db9903cf88e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh@1.81.0.1:", type=("build", "run"))
