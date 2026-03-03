# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcal(RPackage):
	"""Calibration of P-Values for Point Null Hypothesis Testing

	Calibrate p-values under a robust perspective using the methods developed
    by Sellke, Bayarri, and Berger (2001) <doi:10.1198/000313001300339950> and obtain 
    measures of the evidence provided by the data in favor of point null hypotheses 
    which are safer and more straightforward to interpret.
	"""
	
	homepage = "https://pedro-teles-fonseca.github.io/pcal/"
	cran = "pcal" 

	version("1.0.0", md5="2c8940f0645146850280c94706528d83")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
