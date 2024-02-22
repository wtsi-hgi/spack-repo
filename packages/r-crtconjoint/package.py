# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrtconjoint(RPackage):
	"""Conditional Randomization Testing (CRT) Approach for Conjoint
Analysis

	Computes p-value according to the CRT using the HierNet test statistic. For more details, see Ham, Imai, Janson (2022) "Using Machine Learning to Test Causal Hypotheses in Conjoint Analysis" <arXiv:2201.08343>.
	"""
	
	homepage = "https://github.com/daewoongham97/CRTConjoint"
	cran = "CRTConjoint" 

	version("0.1.0", md5="6931554696334a9dc3515202e55409f5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
