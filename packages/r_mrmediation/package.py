# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrmediation(RPackage):
	"""A Causal Mediation Method with Methylated Region (MR) as the
Mediator

	A causal mediation approach under the counterfactual framework 
    to test the significance of total, direct and indirect effects. In this approach, 
    a group of methylated sites from a predefined region are utilized as the mediator, 
    and the functional transformation is used to reduce the possible high dimension 
    in the region-based methylated sites and account for their location information.
	"""
	
	cran = "MRmediation" 

	version("1.0.1", md5="ad2ab3441a8afade9624cdfe121a4f49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
