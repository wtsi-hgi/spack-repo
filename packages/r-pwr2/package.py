# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwr2(RPackage):
	"""Power and Sample Size Analysis for One-way and Two-way ANOVA
Models

	User friendly functions for power and sample size analysis at one-way and two-way ANOVA settings take either effect size or delta and sigma as arguments. They are designed for both one-way and two-way ANOVA settings. In addition, a function for plotting power curves is available for power comparison, which can be easily visualized by statisticians and clinical researchers.
	"""
	
	cran = "pwr2" 

	version("1.0", md5="69574bc5977e7602d519c6c50896a2c0", url="https://cran.r-project.org/src/contrib/pwr2_1.0.tar.gz")

