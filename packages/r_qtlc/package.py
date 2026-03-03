# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtlc(RPackage):
	"""Densitometric Analysis of Thin-Layer Chromatography Plates

	Densitometric evaluation of the photo-archived quantitative thin-layer chromatography (TLC) plates.
	"""
	
	cran = "qtlc" 

	version("1.0", md5="3ebf2848984bc975709b47cb07d098a0")

	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
