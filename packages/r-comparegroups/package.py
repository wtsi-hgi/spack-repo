# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparegroups(RPackage):
	"""Descriptive Analysis by Groups

	Create data summaries for quality control, extensive reports for exploring data, as well as publication-ready univariate or bivariate tables in several formats (plain text, HTML,LaTeX, PDF, Word or Excel. Create figures to quickly visualise the distribution of your data (boxplots, barplots, normality-plots, etc.). Display statistics (mean, median, frequencies, incidences, etc.). Perform the appropriate tests (t-test, Analysis of variance, Kruskal-Wallis, Fisher, log-rank, ...) depending on the nature of the described variable (normal, non-normal or qualitative). Summarize genetic data (Single Nucleotide Polymorphisms) data displaying Allele Frequencies and performing Hardy-Weinberg Equilibrium tests among other typical statistics and tests for these kind of data.
	"""
	
	homepage = "https://isubirana.github.io/compareGroups/"
	cran = "compareGroups" 

	version("4.8.0", md5="75fd7f131ad91fffd760b73ce7fdcd1a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-hardyweinberg", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
