# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThregi(RPackage):
	"""Threshold Regression for Interval-Censored Data with a Cure Rate
Option

	Fit a threshold regression model for Interval Censored Data based on the first-hitting-time of a boundary by the sample path of a Wiener diffusion process. The threshold regression methodology is well suited to applications involving survival and time-to-event data.
	"""
	
	cran = "thregI" 

	version("1.0.4", md5="ef2e7aac13829b5208dd237d236349be")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
