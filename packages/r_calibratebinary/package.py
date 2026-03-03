# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibratebinary(RPackage):
	"""Calibration for Computer Experiments with Binary Responses

	Performs the calibration procedure proposed by Sung et al. (2018+) <arXiv:1806.01453>. This calibration method is particularly useful when the outputs of both computer and physical experiments are binary and the estimation for the calibration parameters is of interest.
	"""
	
	cran = "calibrateBinary" 

	version("0.1", md5="1f1133296560fc019b436f992bc571c0")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-gpfit", type=("build", "run"))
	depends_on("r-gelnet", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
