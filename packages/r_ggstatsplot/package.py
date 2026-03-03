# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstatsplot(RPackage):
	"""'ggplot2' Based Plots with Statistical Details

	Extension of 'ggplot2', 'ggstatsplot' creates graphics with
    details from statistical tests included in the plots themselves. It
    provides an easier syntax to generate information-rich plots for
    statistical analysis of continuous (violin plots, scatterplots,
    histograms, dot plots, dot-and-whisker plots) or categorical (pie and
    bar charts) data. Currently, it supports the most common types of
    statistical approaches and tests: parametric, nonparametric, robust,
    and Bayesian versions of t-test/ANOVA, correlation analyses,
    contingency table analysis, meta-analysis, and regression analyses.
    References: Patil (2021) <doi:10.21105/joss.03236>.
	"""
	
	homepage = "https://indrajeetpatil.github.io/ggstatsplot/"
	cran = "ggstatsplot" 

	version("0.12.2", md5="89a3ec2d69e7732a08670df9ce923c9d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-correlation@0.8.4:", type=("build", "run"))
	depends_on("r-datawizard@0.9.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-ggcorrplot@0.1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-ggrepel@0.9.5:", type=("build", "run"))
	depends_on("r-ggside@0.2.3:", type=("build", "run"))
	depends_on("r-ggsignif@0.6.4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-insight@0.19.7:", type=("build", "run"))
	depends_on("r-paletteer@1.5:", type=("build", "run"))
	depends_on("r-parameters@0.21.3:", type=("build", "run"))
	depends_on("r-patchwork@1.2:", type=("build", "run"))
	depends_on("r-performance@0.10.8:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-statsexpressions@1.5.3:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
