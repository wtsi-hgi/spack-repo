# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemospec2d(RPackage):
	"""Exploratory Chemometrics for 2D Spectroscopy

	A collection of functions for exploratory chemometrics of 2D spectroscopic data sets such as COSY (correlated spectroscopy) and HSQC (heteronuclear single quantum coherence) 2D NMR (nuclear magnetic resonance) spectra. 'ChemoSpec2D' deploys methods aimed primarily at classification of samples and the identification of spectral features which are important in distinguishing samples from each other. Each 2D spectrum (a matrix) is treated as the unit of observation, and thus the physical sample in the spectrometer corresponds to the  sample from a statistical perspective.  In addition to chemometric tools, a few tools are provided for plotting 2D spectra, but these are not intended to replace the functionality typically available on the spectrometer. 'ChemoSpec2D' takes many of its cues from 'ChemoSpec' and tries to create consistent graphical output and to be very user friendly.
	"""
	
	homepage = "https://github.com/bryanhanson/ChemoSpec2D"
	cran = "ChemoSpec2D" 

	version("0.5.0", md5="54f98f47630257a8f62199c9439fd984")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chemospecutils@1:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-readjdx", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
