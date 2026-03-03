# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiosnr(RPackage):
	"""Bioacoustic Basic Operations with Decibels and the Passive Sonar
Equation

	A beginners toolbox to help those in ecology who want to deepen their understanding or utilize Bioacoustics in their work. The package has a number of utilizations from calculating frequency from waveform, performing operations in dB, and determining acoustic range of recorders. The majority of this package is based on key concepts learned from the K. Lisa Yang Center for Conservation Bioacoustics at Cornell University and their associated course: Introduction to Bioacoustics course. More information can be found within the walk through vignettes at <https://github.com/MattyD797/bioSNR/tree/main/vignettes>.
	"""
	
	cran = "bioSNR" 

	version("1.0", md5="b4b2bb0c0c12dbbdf5018ae67f7ccb8f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
