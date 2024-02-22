# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeqr(RPackage):
	"""Target Equivalence Range Design

	The TEQR package contains software to calculate the operating characteristics for the TEQR and the ACT designs.The TEQR (toxicity equivalence range) design is a toxicity based cumulative cohort design with added safety rules. The ACT (Activity constrained for toxicity) design  is also a cumulative cohort design with additional safety rules. The unique feature of this design is that dose is escalated based on lack of activity rather than on lack of toxicity and is de-escalated only if an unacceptable level of toxicity is experienced.
	"""
	
	cran = "TEQR" 

	version("6.0-0", md5="0a606cada5c624b3de90c03f39af92fe")

