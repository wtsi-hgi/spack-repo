# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardinalio(RPackage):
	"""Read and write mass spectrometry imaging files

	Fast and efficient reading and writing of mass spectrometry imaging data files. Supports imzML and Analyze 7.5 formats. Provides ontologies for mass spectrometry imaging.
	"""
	
	homepage = "http://www.cardinalmsi.org"
	bioc = "CardinalIO"

	version("1.6.0", commit="01525c5ae72d6bf4ccfd1fb1734ba98e518946e3")
	version("1.0.0", commit="161a24aa0ec1ec0ce344aec033dcd998fd668708")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-matter", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
