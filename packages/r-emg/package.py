# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmg(RPackage):
	"""Exponentially Modified Gaussian (EMG) Distribution

	Provides basic distribution functions for a mixture model of a Gaussian and exponential distribution.
	"""
	
	cran = "emg" 

	version("1.0.9", md5="fdb540f0383f7a7f0eb4ed66e32cfcea")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
