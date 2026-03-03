# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdslSufa(RPackage):
	"""Simplified UFA

	A simplified version of the 'IDSL.UFA' package to calculate isotopic profiles and adduct formulas from molecular formulas with no dependency on other R packages for online tools and educational mass spectrometry courses. The 'IDSL.SUFA' package also provides an ancillary module to process user-defined adduct formulas.
	"""
	
	homepage = "https://github.com/idslme/idsl.sufa"
	cran = "IDSL.SUFA" 

	version("1.3", md5="0b3a779b44df871e0dc605c45a4fe695")

	depends_on("r@3.5:", type=("build", "run"))
