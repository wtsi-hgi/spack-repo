# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTts(RPackage):
	"""Master Curve Estimates Corresponding to Time-Temperature
Superposition

	Time-Temperature Superposition analysis is often applied to frequency modulated data obtained by Dynamic
		Mechanic Analysis (DMA) and Rheometry in the analytical chemistry and physics
		areas. These techniques provide estimates of material mechanical properties
		(such as moduli) at different temperatures in a wider range of time. This
		package provides the Time-Temperature superposition Master Curve at a referred
		temperature by the three methods: the two wider used methods, Arrhenius based
		methods and WLF, and the newer methodology based on derivatives procedure.
		The Master Curve is smoothed by B-splines basis. The package output is composed
		of plots of experimental data, horizontal and vertical shifts, TTS data, and TTS
		data fitted using B-splines with bootstrap confidence intervals.
	"""
	
	cran = "TTS" 

	version("1.1", md5="72ccddbc07dfa7299d3a46e620c3b071")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
