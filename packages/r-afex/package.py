# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfex(RPackage):
	"""Analysis of Factorial Experiments.

	Convenience functions for analyzing factorial experiments using ANOVA or
	mixed models. aov_ez(), aov_car(), and aov_4() allow specification of
	between, within (i.e., repeated-measures), or mixed (i.e., split-plot)
	ANOVAs for data in long format (i.e., one observation per row),
	automatically aggregating multiple observations per individual and cell of
	the design. mixed() fits mixed models using lme4::lmer() and computes
	p-values for all fixed effects using either Kenward-Roger or Satterthwaite
	approximation for degrees of freedom (LMM only), parametric bootstrap (LMMs
	and GLMMs), or likelihood ratio tests (LMMs and GLMMs).  afex_plot()
	provides a high-level interface for interaction or one-way plots using
	ggplot2, combining raw data and model estimates. afex uses type 3 sums of
	squares as default (imitating commercial statistical software)."""

	cran = "afex"

	version("1.3-0", md5="928302f51d421605f77527a897a605d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4@1.1.8:", type=("build", "run"))
	depends_on("r-pbkrtest@0.4.1:", type=("build", "run"))
	depends_on("r-lmertest@3.0.0:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
