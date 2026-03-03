# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClonerate(RPackage):
	"""Estimate Growth Rates from Phylogenetic Trees

	Quickly estimate the net growth rate of a
    population or clone whose growth can be approximated by a birth-death
    branching process.  Input should be phylogenetic tree(s) of clone(s) with
    edge lengths corresponding to either time or mutations. Based on
    coalescent results in Johnson et al. (2023) <doi:10.1093/bioinformatics/btad561>. Simulation
    techniques as well as growth rate methods build on prior work from
    Lambert A. (2018) <doi:10.1016/j.tpb.2018.04.005> and Stadler T. (2009)
    <doi:10.1016/j.jtbi.2009.07.018>.
	"""
	
	homepage = "https://github.com/bdj34/cloneRate"
	cran = "cloneRate" 

	version("0.2.3", md5="1e774c949ba03b121e2407940c6cb437")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ape@4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rmpfr@0.8:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
