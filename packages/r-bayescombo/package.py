# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayescombo(RPackage):
	"""Bayesian Evidence Combination

	Combine diverse evidence across multiple studies to test a high level scientific theory. The methods can also be used as an alternative to a standard meta-analysis.
	"""
	
	homepage = "https://github.com/stanlazic/BayesCombo"
	cran = "BayesCombo" 

	version("1.0", md5="821d0c78d193db5b1c05b8f471c78a57")

	depends_on("r@2.10:", type=("build", "run"))
