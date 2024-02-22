# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvcrand(RPackage):
	"""Efficient Design and Analysis of Cluster Randomized Trials

	Constrained randomization by Raab and Butcher (2001) <doi:10.1002/1097-0258(20010215)20:3%3C351::AID-SIM797%3E3.0.CO;2-C> 
            is suitable for cluster randomized trials (CRTs) with a
            small number of clusters (e.g., 20 or fewer). The procedure of
            constrained randomization is based on the baseline values of some
            cluster-level covariates specified. The intervention effect on
            the individual outcome can then be analyzed through
            clustered permutation test introduced by Gail, et al. (1996) <doi:10.1002/(SICI)1097-0258(19960615)15:11%3C1069::AID-SIM220%3E3.0.CO;2-Q>. 
            Motivated from Li, et al. (2016) <doi:10.1002/sim.7410>, the package performs constrained randomization on the baseline
            values of cluster-level covariates and clustered permutation test on the individual-level outcomes for cluster randomized trials. 
	"""
	
	cran = "cvcrand" 

	version("0.1.1", md5="1cc3718c1159da9f310edb6c54312423")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
