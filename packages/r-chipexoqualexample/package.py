# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipexoqualexample(RPackage):
	"""Example data for the ChIPexoQual package, which implements a quality control pipeline for ChIP-exo data

	Data for the ChIPexoQual package, consisting of (3) chromosome 1 aligned reads from a ChIP-exo experiment for FoxA1 in mouse liver cell lines aligned to the mm9 genome.
	"""
	
	homepage = "http://www.github.com/keleslab/ChIPexoQualExample"
	bioc = "ChIPexoQualExample"

	version("1.32.0", commit="352ef100c58de19d5e22eff2a8e0adc15f906bf3")
	version("1.26.0", commit="a18e0d93073a0f96aee7410c9a07b3d66ab388c7")

	depends_on("r@3.3:", type=("build", "run"))

