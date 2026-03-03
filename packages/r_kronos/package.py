# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKronos(RPackage):
	"""Microbiome Oriented Circadian Rhythm Analysis Toolkit

	The goal of 'kronos' is to provide an easy-to-use framework to analyse circadian or otherwise rhythmic data using the familiar R linear modelling syntax, while taking care of the trigonometry under the hood. 
	"""
	
	homepage = "https://github.com/thomazbastiaanssen/kronos"
	cran = "kronos" 

	version("1.0.0", md5="682a570686bfa1381a24d41bff7755b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
