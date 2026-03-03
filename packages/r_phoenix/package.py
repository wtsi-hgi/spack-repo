# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhoenix(RPackage):
	"""The Phoenix Pediatric Sepsis and Septic Shock Criteria

	Implementation of the Phoenix and Phoenix-8 Sepsis Criteria as
    described in "Development and Validation of the Phoenix Criteria for
    Pediatric Sepsis and Septic Shock" by Sanchez-Pinto, Bennett, DeWitt,
    Russell et al. (2024) <doi:10.1001/jama.2024.0196> (Drs. Sanchez-Pinto
    and Bennett contributed equally to this manuscript; Dr. DeWitt and Mr.
    Russell contributed equally to the manuscript) and "International Consensus
    Criteria for Pediatric Sepsis and Septic Shock" by Schlapbach, Watson,
    Sorce, Argent, et al. (2024) <doi:10.1001/jama.2024.0179> (Drs Schlapbach,
    Watson, Sorce, and Argent contributed equally).
	"""
	
	homepage = "https://github.com/CU-DBMI-Peds/phoenix/"
	cran = "phoenix" 

	version("1.0.0", md5="a1b2720e5a86847172cfb26aa575bc08")

	depends_on("r@3.5:", type=("build", "run"))
