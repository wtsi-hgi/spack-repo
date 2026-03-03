# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJops(RPackage):
	"""Practical Smoothing with P-Splines

	Functions and data to reproduce all plots in the book "Practical Smoothing. 
 The Joys of P-splines" by Paul H.C. Eilers and Brian D. Marx (2021, ISBN:978-1108482950). 
	"""
	
	cran = "JOPS" 

	version("0.1.19", md5="238d28ee4c58e69a7fa1271063b706de")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-spats@1.0.13:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-fds", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-semipar", type=("build", "run"))
