# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNdl(RPackage):
	"""Naive Discriminative Learning

	Naive discriminative learning implements learning and
    classification models based on the Rescorla-Wagner equations and their
    equilibrium equations.
	"""
	
	cran = "ndl" 

	version("0.2.18", md5="b1810ad36d0e5462a70d2a85df08a3f7")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
