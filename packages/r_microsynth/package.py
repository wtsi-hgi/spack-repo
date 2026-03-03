# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrosynth(RPackage):
	"""Synthetic Control Methods with Micro- And Meso-Level Data

	A generalization of the 'Synth' package that is designed for
    data at a more granular level (e.g., micro-level). Provides functions
    to construct weights (including propensity score-type weights) and run
    analyses for synthetic control methods with micro- and meso-level
    data; see Robbins, Saunders, and Kilmer (2017)
    <doi:10.1080/01621459.2016.1213634> and Robbins and Davenport (2021)
    <doi:10.18637/jss.v097.i02>.
	"""
	
	cran = "microsynth" 

	version("2.0.44", md5="8cfde1e49565f86116123d764f13c0ca")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
