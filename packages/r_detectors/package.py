# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetectors(RPackage):
	"""Prediction Data from GPT Detectors

	Researchers carried out a series of experiments passing a number 
  of essays to different GPT detection models. Juxtaposing detector predictions 
  for papers written by native and non-native English writers, the authors argue 
  that GPT detectors disproportionately classify real writing from non-native 
  English writers as AI-generated. 
	"""
	
	homepage = "https://simonpcouch.github.io/detectors/"
	cran = "detectors" 

	version("0.1.0", md5="5f89c2f57f6715e3f86163827a2b0d75")

	depends_on("r@2.10:", type=("build", "run"))
