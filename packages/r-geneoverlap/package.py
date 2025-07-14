# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneoverlap(RPackage):
	"""Test and visualize gene overlaps

	Test two sets of gene lists and visualize the results.
	"""
	
	homepage = "http://shenlab-sinai.github.io/shenlab-sinai/"
	bioc = "GeneOverlap"

	version("1.44.0", commit="f5c96e4e116d33d4d5d1898fda020e3b8f74219d")
	version("1.38.0", commit="016133771631f7a2c128a2245d5c62e0b7adf32b")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
