# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfishdraw(RPackage):
	"""Automatically Generated Fish Drawings via JavaScript

	Automatic generation of fish drawings based on JavaScript library <https://github.com/LingDong-/fishdraw>, including JavaScript code for dynamic generation of fish drawings.
	"""
	
	homepage = "https://github.com/Otoliths/rfishdraw"
	cran = "rfishdraw" 

	version("0.1.0", md5="2631d2026cea3fb20d72be06edc20e45")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
