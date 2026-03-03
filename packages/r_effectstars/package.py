# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REffectstars(RPackage):
	"""Visualization of Categorical Response Models

	Notice: The package EffectStars2 provides a more up-to-date implementation of effect stars! EffectStars provides functions to visualize regression models with categorical response as proposed by Tutz and Schauberger (2013) <doi:10.1080/10618600.2012.701379>. The effects of the variables are plotted with star plots in order to allow for an optical impression of the fitted model.
	"""
	
	cran = "EffectStars" 

	version("1.9-1", md5="e6e576f3dda455d0c0920a4c62d05db6")

	depends_on("r-vgam", type=("build", "run"))
