# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmplik2(RPackage):
	"""Empirical Likelihood Ratio Test for Two Samples with Censored
Data

	Calculates the p-value for a mean-type hypothesis (or multiple mean-type hypotheses) based on 
        two samples with possible censored data.
	"""
	
	cran = "emplik2" 

	version("1.32", md5="58c97ccdd11fd15e50a50915fa75192b", url="https://cran.r-project.org/src/contrib/emplik2_1.32.tar.gz")

	depends_on("r@3.2.5:", type=("build", "run"))
