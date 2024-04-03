# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatsexpressions(RPackage):
	"""Tidy Dataframes and Expressions with Statistical Details

	Utilities for producing dataframes with rich details for the
    most common types of statistical approaches and tests: parametric,
    nonparametric, robust, and Bayesian t-test, one-way ANOVA, correlation
    analyses, contingency table analyses, and meta-analyses. The
    functions are pipe-friendly and provide a consistent syntax to work
    with tidy data. These dataframes additionally contain expressions with
    statistical details, and can be used in graphing packages. This
    package also forms the statistical processing backend for
    'ggstatsplot'. References: Patil (2021) <doi:10.21105/joss.03236>.
	"""
	
	homepage = "https://indrajeetpatil.github.io/statsExpressions/"
	cran = "statsExpressions" 

	version("1.5.4", md5="8acc0a1999627212eededa95102b0c41")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-afex@1.3.1:", type=("build", "run"))
	depends_on("r-bayesfactor@0.9.12.4.7:", type=("build", "run"))
	depends_on("r-correlation@0.8.4:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-effectsize@0.8.6:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-insight@0.19.9:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parameters@0.21.6:", type=("build", "run"))
	depends_on("r-performance@0.10.9:", type=("build", "run"))
	depends_on("r-pmcmrplus", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3.1:", type=("build", "run"))
	depends_on("r-withr@3:", type=("build", "run"))
	depends_on("r-wrs2", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
