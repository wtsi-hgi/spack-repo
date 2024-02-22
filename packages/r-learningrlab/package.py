# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearningrlab(RPackage):
	"""Statistical Learning Functions

	Aids in learning statistical functions incorporating the result of calculus done with each function and how they are obtained, that is, which equation and variables are used. Also for all these equations and their related variables detailed explanations and interactive exercises are also included. All these characteristics allow to the package user to improve the learning of statistics basics by means of their use.
	"""
	
	cran = "LearningRlab" 

	version("2.4", md5="da592ad0f90900e36ec51b3a7a774e5a")

	depends_on("r-magick", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
