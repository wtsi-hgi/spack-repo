# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForetell(RPackage):
	"""Projecting Customer Retention Based on Fader and Hardie
Probability Models

	Project Customer Retention based on Beta Geometric, Beta Discrete Weibull and Latent Class 
    Discrete Weibull Models.This package is based on Fader and Hardie (2007) 
    <doi:10.1002/dir.20074> and Fader and Hardie et al. (2018) <doi:10.1016/j.intmar.2018.01.002>.
	"""
	
	cran = "foretell" 

	version("0.2.0", md5="a01001119742d64d9e8b1fdd63cfacb1")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
