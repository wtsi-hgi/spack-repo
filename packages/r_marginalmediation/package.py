# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarginalmediation(RPackage):
	"""Marginal Mediation

	Provides the ability to perform "Marginal Mediation"--mediation
   wherein the indirect and direct effects are in terms of the average marginal effects 
   (Bartus, 2005, <https://EconPapers.repec.org/RePEc:tsj:stataj:v:5:y:2005:i:3:p:309-329>). 
   The style of the average marginal effects stems from Thomas Leeper's work on the "margins" package.
   This framework allows the use of categorical mediators and outcomes with little change in interpretation
   from the continuous mediators/outcomes. See <doi:10.13140/RG.2.2.18465.92001> for more details 
   on the method.
	"""
	
	cran = "MarginalMediation" 

	version("0.7.2", md5="bc3ccc2d21c57e4508892a1359a791d4")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-furniture", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
