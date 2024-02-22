# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterpretmsspectrum(RPackage):
	"""Interpreting High Resolution Mass Spectra

	High resolution mass spectrometry yields often large data sets of 
    spectra from compounds which are not present in available libraries. These 
    spectra need to be annotated and interpreted.
    'InterpretMSSpectrum' provides a set of functions to perform such tasks for 
    Electrospray-Ionization and Atmospheric-Pressure-Chemical-Ionization derived 
    data in positive and negative ionization mode.
	"""
	
	homepage = "https://github.com/janlisec/InterpretMSSpectrum"
	cran = "InterpretMSSpectrum" 

	version("1.4.5", md5="37cbc602987c5f65c9457da0968c828d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-envipat", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
