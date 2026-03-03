# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetmstatistic(RPackage):
	"""Quantifying Systematic Heterogeneity in Meta-Analysis

	Quantifying systematic heterogeneity in meta-analysis using R.
    The M statistic aggregates heterogeneity information across multiple
    variants to, identify systematic heterogeneity patterns and their direction
    of effect in meta-analysis. It's primary use is to identify outlier studies,
    which either show "null" effects or consistently show stronger or weaker
    genetic effects than average across, the panel of variants examined in a
    GWAS meta-analysis. In contrast to conventional heterogeneity metrics
    (Q-statistic, I-squared and tau-squared) which measure random heterogeneity
    at individual variants, M measures systematic (non-random)
    heterogeneity across multiple independently associated variants. Systematic
    heterogeneity can arise in a meta-analysis due to differences in the study
    characteristics of participating studies. Some of the differences may
    include: ancestry, allele frequencies, phenotype definition, age-of-disease
    onset, family-history, gender, linkage disequilibrium and quality control
    thresholds. See <https://magosil86.github.io/getmstatistic/> for statistical
    statistical theory, documentation and examples.
	"""
	
	homepage = "https://magosil86.github.io/getmstatistic/"
	cran = "getmstatistic" 

	version("0.2.2", md5="4e5b328bc4036c7e7cb08f05a911648c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
	depends_on("r-gridextra@0.9.1:", type=("build", "run"))
	depends_on("r-gtable@0.1.2:", type=("build", "run"))
	depends_on("r-metafor@1.9.6:", type=("build", "run"))
	depends_on("r-psych@1.5.1:", type=("build", "run"))
	depends_on("r-stargazer@5.1:", type=("build", "run"))
