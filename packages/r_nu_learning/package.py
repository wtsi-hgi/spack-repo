# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNuLearning(RPackage):
	"""Nonparametric and Unsupervised Learning from Cross-Sectional
Observational Data

	Especially when cross-sectional data are observational, effects of treatment selection
  bias and confounding are best revealed by using Nonparametric and Unsupervised methods to
  "Design" the analysis of the given data ...rather than the collection of "designed data".
  Specifically, the "effect-size distribution" that best quantifies a potentially causal
  relationship between a numeric y-Outcome variable and either a binary t-Treatment or
  continuous e-Exposure variable needs to consist of BLOCKS of relatively well-matched
  experimental units (e.g. patients) that have the most similar X-confounder characteristics.
  Since our NU Learning approach will form BLOCKS by "clustering" experimental units in
  confounder X-space, the implicit statistical model for learning is One-Way ANOVA. Within
  Block measures of effect-size are then either [a] LOCAL Treatment Differences (LTDs) between
  Within-Cluster y-Outcome Means ("new" minus "control") when treatment choice is
  Binary or else [b] LOCAL Rank Correlations (LRCs) when the e-Exposure variable is numeric
  with (hopefully many) more than two levels. An Instrumental Variable (IV) method is also
  provided so that Local Average y-Outcomes (LAOs) within BLOCKS may also contribute
  information for effect-size inferences when X-Covariates are assumed to influence Treatment
  choice or Exposure level but otherwise have no direct effects on y-Outcomes. Finally, a
  "Most-Like-Me" function provides histograms of effect-size distributions to aid
  Doctor-Patient (or Researcher-Society) communications about Heterogeneous Outcomes.
  Obenchain and Young (2013) <doi:10.1080/15598608.2013.772821>; Obenchain, Young and Krstic
  (2019) <doi:10.1016/j.yrtph.2019.104418>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "NU.Learning" 

	version("1.5", md5="1a99077dacebde38565adcb33de41605")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
