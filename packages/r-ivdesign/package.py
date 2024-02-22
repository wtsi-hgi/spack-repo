# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvdesign(RPackage):
	"""Hypothesis Testing in Cluster-Randomized Encouragement Designs

	An implementation of randomization-based hypothesis 
    testing for three different estimands in a cluster-randomized 
    encouragement experiment. The three estimands include (1) testing
    a cluster-level constant proportional treatment effect (Fisher's
    sharp null hypothesis), (2) pooled effect ratio, and (3) average 
    cluster effect ratio. To test the third estimand, user needs to install
    'Gurobi' (>= 9.0.1) optimizer via its R API. Please refer to 
    <https://www.gurobi.com/documentation/9.0/refman/ins_the_r_package.html>.
	"""
	
	cran = "ivdesign" 

	version("0.1.0", md5="9c787ffcf8fabf37a65486bc46e4cd09")

	depends_on("r@2.10:", type=("build", "run"))
