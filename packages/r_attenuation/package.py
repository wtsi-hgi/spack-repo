# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAttenuation(RPackage):
	"""Correcting for Attenuation Due to Measurement Error

	Confidence curves, confidence intervals and p-values for 
   correlation coefficients corrected for attenuation due to measurement error.
   Implements the methods described in Moss (2019, <arxiv:1911.01576>).
	"""
	
	homepage = "https://github.com/JonasMoss/attenuation/"
	cran = "attenuation" 

	version("1.0.0", md5="788fcff488577dee88485df508b3ed42")

