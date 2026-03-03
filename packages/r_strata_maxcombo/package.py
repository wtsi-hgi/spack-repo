# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrataMaxcombo(RPackage):
	"""Stratified Max-Combo Test

	Non-proportional hazard (NPH) is commonly observed in immuno-oncology studies, where the survival curves of the treatment and control groups show delayed separation. To properly account for NPH, several statistical methods have been developed. One such method is Max-Combo test, which is a straightforward and flexible hypothesis testing method that can simultaneously test for constant, early, middle, and late treatment effects. However, the majority of the Max-Combo test performed in clinical studies are unstratified, ignoring the important prognostic stratification factors. To fill this gap, we have developed an R package for stratified Max-Combo testing that accounts for stratified baseline factors. Our package explores various methods for calculating combined test statistics, estimating joint distributions, and determining the p-values.
	"""
	
	cran = "strata.MaxCombo" 

	version("0.0.1", md5="bbd2385cee15c607231b8f3260f4ea75")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
