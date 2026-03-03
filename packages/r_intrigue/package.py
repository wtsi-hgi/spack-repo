# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrigue(RPackage):
	"""Quantify and Control Reproducibility in High-Throughput
Experiments

	Estimate the proportions of the null and the reproducibility and
    non-reproducibility of the signal group for the input data set. The Bayes factor
    calculation and EM (Expectation Maximization) algorithm procedures are also
    included.
	"""
	
	cran = "INTRIGUE" 

	version("0.1.0", md5="8a334f98e406007a85fc82d521c5065a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
