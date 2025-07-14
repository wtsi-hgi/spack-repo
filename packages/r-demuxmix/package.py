# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemuxmix(RPackage):
	"""Demultiplexing oligo-barcoded scRNA-seq data using regression mixture models

	A package for demultiplexing single-cell sequencing experiments of pooled cells labeled with barcode oligonucleotides. The package implements methods to fit regression mixture models for a probabilistic classification of cells, including multiplet detection. Demultiplexing error rates can be estimated, and methods for quality control are provided.
	"""
	
	homepage = "https://github.com/huklein/demuxmix"
	bioc = "demuxmix"

	version("1.10.0", commit="e0d9b04dfe639807ddd7e26aa6a6abb091065c2d")
	version("1.4.0", commit="4cd7194d9c00735dd9032066220c75e4eac0e3d8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
