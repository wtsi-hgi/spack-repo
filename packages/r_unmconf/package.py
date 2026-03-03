# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnmconf(RPackage):
	"""Modeling with Unmeasured Confounding

	Fit and assess Bayesian multi-staged regression models that account 
    for unmeasured confounders using JAGS.
	"""
	
	cran = "unmconf" 

	version("0.1.0", md5="92dbaf22863be91efe9a0bc7d45a1d1e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
