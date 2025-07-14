# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaggedexperiment(RPackage):
	"""Representation of Sparse Experiments and Assays Across Samples

	This package provides a flexible representation of copy number, mutation, and other data that fit into the ragged array schema for genomic location data. The basic representation of such data provides a rectangular flat table interface to the user with range information in the rows and samples/specimen in the columns. The RaggedExperiment class derives from a GRangesList representation and provides a semblance of a rectangular dataset.
	"""
	
	bioc = "RaggedExperiment"

	version("1.32.2", commit="96ccbb9284b73b4907680cb9ae575becd619e673")
	version("1.26.0", commit="1da7790d0d1bdcfe85d87c864d7aefe6da5d58d1")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.37.17:", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
