# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdecob(RPackage):
	"""Event Detection Using Confidence Bounds

	Detects sustained change in digital bio-marker data using
    simultaneous confidence bands. Accounts for noise using an auto-regressive
    model. Based on Buehlmann (1998) "Sieve bootstrap for smoothing in
    nonstationary time series" <doi:10.1214/aos/1030563978>.
	"""
	
	cran = "edecob" 

	version("1.2.2", md5="3752de1593859d1ec5d79eae3bf35538")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
