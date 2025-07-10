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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CardinalIO_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CardinalIO/CardinalIO_1.0.0.tar.gz"]

	version("1.0.0", sha256="c6569a101b121b1445c785f7cb17214a55d1630ac0a774e7e5e32ca199293d4f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-matter", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
