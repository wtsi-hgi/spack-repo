# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmv(RPackage):
	"""The 'jamovi' Analyses

	A suite of common statistical methods such as descriptives,
    t-tests, ANOVAs, regression, correlation matrices, proportion tests,
    contingency tables, and factor analysis. This package is also useable from
    the 'jamovi' statistical spreadsheet (see <https://www.jamovi.org> for more
    information).
	"""
	
	cran = "jmv" 

	version("2.4.11", md5="bae8bdb33f061acab82ec8cae6a7774e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-jmvcore@2.4.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-car@3:", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-pmcmr", type=("build", "run"))
	depends_on("r-emmeans@1.4.2:", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-vcdextra", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-psych@1.7.5:", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-afex@0.28.0:", type=("build", "run"))
	depends_on("r-mvnormtest", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
