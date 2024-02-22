# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHilbertsimilarity(RPackage):
	"""Hilbert Similarity Index for High Dimensional Data

	Quantifying similarity between high-dimensional single cell samples is challenging, and usually requires
    some simplifying hypothesis to be made. By transforming the high dimensional space into a high dimensional grid,
    the number of cells in each sub-space of the grid is characteristic of a given sample. Using a Hilbert curve
    each sample can be visualized as a simple density plot, and the distance between samples can be calculated from
    the distribution of cells using the Jensen-Shannon distance. Bins that correspond to significant differences
    between samples can identified using a simple bootstrap procedure.
	"""
	
	homepage = "http://github.com/yannabraham/hilbertSimilarity"
	cran = "hilbertSimilarity" 

	version("0.4.3", md5="447ac96da9e020a681503b3c1874e180")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
