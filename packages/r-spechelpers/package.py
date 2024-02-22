# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpechelpers(RPackage):
	"""Spectroscopy Related Utilities

	Utility functions for spectroscopy. 1. Functions to simulate
    spectra for use in teaching or testing. 2. Functions to process files created by
    'LoggerPro' and 'SpectraSuite' software.
	"""
	
	homepage = "https://github.com/bryanhanson/SpecHelpers"
	cran = "SpecHelpers" 

	version("0.2.7", md5="722665cc31b470c3f592a33a50cd96b4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
