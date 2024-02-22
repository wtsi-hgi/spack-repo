# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenebgm(RPackage):
	"""EBGM Disproportionality Scores for Adverse Event Data Mining

	An implementation of DuMouchel's (1999) <doi:10.1080/00031305.1999.10474456>
  Bayesian data mining method for the market basket problem.
  Calculates Empirical Bayes Geometric Mean (EBGM) and posterior quantile scores
  using the Gamma-Poisson Shrinker (GPS) model to find unusually large cell
  counts in large, sparse contingency tables. Can be used to find unusually high
  reporting rates of adverse events associated with products. In general, can be
  used to mine any database where the co-occurrence of two variables or items is
  of interest. Also calculates relative and proportional reporting ratios.
  Builds on the work of the 'PhViD' package, from which much of the code is
  derived. Some of the added features include stratification to adjust for
  confounding variables and data squashing to improve computational efficiency.
  Includes an implementation of the EM algorithm for hyperparameter estimation
  loosely derived from the 'mederrRank' package.
	"""
	
	homepage = "https://journal.r-project.org/archive/2017/RJ-2017-063/index.html"
	cran = "openEBGM" 

	version("0.9.1", md5="6994f94fca02fe5c9b869baaf94ad712")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
