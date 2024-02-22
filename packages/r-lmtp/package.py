# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmtp(RPackage):
	"""Non-Parametric Causal Effects of Feasible Interventions Based on
Modified Treatment Policies

	Non-parametric estimators for casual effects based on longitudinal modified treatment 
  policies as described in Diaz, Williams, Hoffman, and Schenck <doi:10.1080/01621459.2021.1955691>, traditional point treatment, 
  and traditional longitudinal effects. Continuous, binary, and categorical treatments are allowed as well are 
  censored outcomes. The treatment mechanism is estimated via a density ratio classification procedure 
  irrespective of treatment variable type. For both continuous and binary outcomes, additive treatment effects 
  can be calculated and relative risks and odds ratios may be calculated for binary outcomes.  
	"""
	
	homepage = "https://github.com/nt-williams/lmtp"
	cran = "lmtp" 

	version("1.3.2", md5="0b24177021bf073104a6f5fefb1d3fec")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-origami", type=("build", "run"))
	depends_on("r-future@1.17:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
