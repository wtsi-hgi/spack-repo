# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreg(RPackage):
	"""Threshold Regression

	Fit a threshold regression model based on the first-hitting-time of a boundary by the sample path of a Wiener diffusion process. The threshold regression methodology is well suited to applications involving survival and time-to-event data.
	"""
	
	cran = "threg" 

	version("1.0.3", md5="377b95c2b4bdf580bb2c210b008040b5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
