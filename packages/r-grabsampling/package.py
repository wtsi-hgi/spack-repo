# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrabsampling(RPackage):
	"""Probability of Detection for Grab Sample Selection

	Functions for obtaining the probability of detection, for grab samples selection by using two different methods such as systematic or random based on two-state Markov chain model. For detection probability calculation, we used results from Bhat, U. and Lal, R. (1988) <doi:10.2307/1427041>.
	"""
	
	homepage = "https://github.com/Mayooran1987/grabsampling"
	cran = "grabsampling" 

	version("1.0.0", md5="3b1c58a96103c161c24a23a84752a00b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
