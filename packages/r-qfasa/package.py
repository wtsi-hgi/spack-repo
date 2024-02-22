# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQfasa(RPackage):
	"""Quantitative Fatty Acid Signature Analysis

	Accurate estimates of the diets of predators are required
    in many areas of ecology, but for many species current methods are
    imprecise, limited to the last meal, and often biased. The diversity
    of fatty acids and their patterns in organisms, coupled with the
    narrow limitations on their biosynthesis, properties of digestion in
    monogastric animals, and the prevalence of large storage reservoirs of
    lipid in many predators, led to the development of quantitative
    fatty acid signature analysis (QFASA) to study predator diets.
	"""
	
	homepage = "https://CRAN.R-project.org/package=QFASA"
	cran = "QFASA" 

	version("1.2.0", md5="3da74e682afa75269369b4b11035ae76")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
	depends_on("r-compositional", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
