# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTse(RPackage):
	"""Total Survey Error

	Calculates total survey error (TSE) for one or more surveys, using common scale-dependent and/or scale-independent metrics.  On TSE, see: Weisberg, Herbert (2005, ISBN:0-226-89128-3); Biemer, Paul (2010) <doi:10.1093/poq/nfq058>.
	"""
	
	cran = "TSE" 

	version("0.1.0", md5="0f4bcde267790c95e7de61fda5ded087")

	depends_on("r@3.5:", type=("build", "run"))
