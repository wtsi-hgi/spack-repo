# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbbayes(RPackage):
	"""Probability and Bayesian Modeling

	Functions and datasets  to accompany J. Albert and J. Hu, "Probability and Bayesian Modeling", CRC Press, (2019, ISBN: 1138492566).
	"""
	
	homepage = "https://github.com/bayesball/ProbBayes"
	cran = "ProbBayes" 

	version("1.1", md5="8b1603b0e5a5493a959721cbd2a31337")

	depends_on("r-learnbayes", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
