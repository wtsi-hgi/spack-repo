# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGginference(RPackage):
	"""Visualise the Results of Inferential Statistics using 'ggplot2'

	Visualise the results of F test to compare two variances, Student's t-test, test of equal or given proportions, Pearson's chi-squared test for count data and test for association/correlation between paired samples.
	"""
	
	homepage = "https://github.com/okgreece/gginference"
	cran = "gginference" 

	version("0.1.3", md5="92382557d8931ad2b2b747fd993ea7d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
