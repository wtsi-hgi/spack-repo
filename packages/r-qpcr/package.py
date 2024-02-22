# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpcr(RPackage):
	"""Modelling and Analysis of Real-Time PCR Data

	Model fitting, optimal model selection and calculation of various features that are essential in the analysis of quantitative real-time polymerase chain reaction (qPCR).
	"""
	
	cran = "qpcR" 

	version("1.4-1", md5="49fbceb2e4cbdf6ce056d4734630c474")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
