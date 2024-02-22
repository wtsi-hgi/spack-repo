# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroupcomparisons(RPackage):
	"""Paired/Unpaired Parametric/Non-Parametric Group Comparisons

	Receives two vectors, computes appropriate function for group comparison (i.e., t-test, Mann-Whitney; equality of variances), and reports the findings (mean/median, standard deviation, test statistic, p-value, effect size) in APA format (Fay, M.P., & Proschan, M.A. (2010)<DOI: 10.1214/09-SS051>).
	"""
	
	cran = "GroupComparisons" 

	version("0.1.0", md5="bf88ade406adc7d1b715769f0ce8250b")

	depends_on("r-car", type=("build", "run"))
