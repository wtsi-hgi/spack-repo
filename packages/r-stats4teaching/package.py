# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStats4teaching(RPackage):
	"""Simulate Pedagogical Statistical Data

	Univariate and multivariate normal data simulation. They also supply a brief summary of the analysis for each experiment/design:
    - Independent samples.
    - One-way and two-way Anova.
    - Paired samples (T-Test & Regression).
    - Repeated measures (Anova & Multiple Regression).
    - Clinical Assay. 
	"""
	
	cran = "stats4teaching" 

	version("0.1.0", md5="9c386fb725b0191a3386102cd91c515c")

	depends_on("r-asbio", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-clustergeneration", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvn", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-rstatix", type=("build", "run"))
