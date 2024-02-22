# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLaterality(RPackage):
	"""Functions to Calculate Common Laterality Statistics in
Primatology

	Calculates and plots Handedness index (HI), absolute HI, mean HI and z-score which are commonly used indexes for the study of hand preference (laterality) in non-human primates.
	"""
	
	cran = "Laterality" 

	version("0.9.4", md5="5327b51e8479bc775fcc079fce7395e6")

	depends_on("r-ade4", type=("build", "run"))
