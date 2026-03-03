# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemographictable(RPackage):
	"""Creating Demographic Table

	Functions for creating demographic table with simple summary
        statistics, with optional comparison(s) over one or more groups.
        Numeric variables are summarized in means, standard deviations,
        medians, inter-quartile-ranges (IQR), skewness, Shapiro-Wilk
        normality test and ranges, and compared using two-sample t-test,
        Wilcoxon test, ANOVA and/or Kruskal-Wallis test.  Logical and
        factor variables are summarized in counts and percentages and
        compared using chi-squared test and/or Fisher's exact test.
	"""
	
	cran = "DemographicTable" 

	version("0.1.6", md5="617a8af4f8a2003d6a7f79bee6a522fe")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
