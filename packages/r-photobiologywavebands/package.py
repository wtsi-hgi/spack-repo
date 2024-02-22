# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologywavebands(RPackage):
	"""Waveband Definitions for UV, VIS, and IR Radiation

	Constructors of waveband objects for commonly used biological
    spectral weighting functions (BSWFs) and for different wavebands describing
    named ranges of wavelengths in the ultraviolet (UV), visible (VIS)
    and infrared (IR) regions of the electromagnetic spectrum.  Part of the
    'r4photobiology' suite, Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/photobiologyWavebands/"
	cran = "photobiologyWavebands" 

	version("0.5.2", md5="1a008d50603842f1069d6d697e5bdaab")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.11:", type=("build", "run"))
