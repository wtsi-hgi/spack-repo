# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfintr(RPackage):
	"""Confidence Intervals

	Calculates classic and/or bootstrap confidence intervals for
    many parameters such as the population mean, variance, interquartile
    range (IQR), median absolute deviation (MAD), skewness, kurtosis,
    Cramer's V, odds ratio, R-squared, quantiles (incl. median),
    proportions, different types of correlation measures, difference in
    means, quantiles and medians. Many of the classic confidence intervals
    are described in Smithson, M. (2003, ISBN: 978-0761924999). Bootstrap
    confidence intervals are calculated with the R package 'boot'. Both
    one- and two-sided intervals are supported.
	"""
	
	homepage = "https://github.com/mayer79/confintr"
	cran = "confintr" 

	version("1.0.2", md5="628fd405c1c04154e90bfd7eca2bfb44")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
