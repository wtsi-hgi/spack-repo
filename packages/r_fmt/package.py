# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmt(RPackage):
	"""Variance Estimation of FMT Method (Fully Moderated T-Statistic)

	The FMT method computes posterior residual variances to be used in
  the denominator of a moderated t-statistic from a linear model analysis of
  gene expression data. It is an extension of the moderated t-statistic
  originally proposed by Smyth (2004) <doi:10.2202/1544-6115.1027>.
  LOESS local regression and empirical Bayesian method are used to estimate
  gene specific prior degrees of freedom and prior variance based on average
  gene intensity levels. The posterior residual variance in the denominator is
  a weighted average of prior and residual variance and the weights are prior
  degrees of freedom and residual variance degrees of freedom. The degrees of
  freedom of the moderated t-statistic is simply the sum of prior and residual
  variance degrees of freedom.
	"""
	
	cran = "fmt" 

	version("2.0", md5="9c5f74e3f7336894c350ad9f90f72e5e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
