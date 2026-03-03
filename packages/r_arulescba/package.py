# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArulescba(RPackage):
	"""Classification Based on Association Rules

	Provides the infrastructure for association rule-based classification including the algorithms 
  CBA, CMAR, CPAR, C4.5, FOIL, PART, PRM, RCAR, and RIPPER to build associative classifiers. 
  Hahsler et al (2019) <doi:10.32614/RJ-2019-048>.
	"""
	
	homepage = "https://github.com/mhahsler/arulesCBA"
	cran = "arulesCBA" 

	version("1.2.5", md5="994d4bddbe81b26a9aeb6f08e42d311a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrix@1.4.0:", type=("build", "run"))
	depends_on("r-arules@1.7.4:", type=("build", "run"))
	depends_on("r-discretization@1.0.1:", type=("build", "run"))
	depends_on("r-glmnet@3.0.0:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
