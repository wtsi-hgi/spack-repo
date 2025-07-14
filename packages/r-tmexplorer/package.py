# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmexplorer(RPackage):
	"""A Collection of Tumour Microenvironment Single-cell RNA Sequencing Datasets and Corresponding Metadata

	This package provides a tool to search and download a collection of tumour microenvironment single-cell RNA sequencing datasets and their metadata. TMExplorer aims to act as a single point of entry for users looking to study the tumour microenvironment at the single cell level. Users can quickly search available datasets using the metadata table and then download the ones they are interested in for analysis.
	"""
	
	bioc = "TMExplorer"

	version("1.18.0", commit="143184d5fef00c2181312b3b31f6d2b660b9c8d8")
	version("1.12.0", commit="3c5926c2caaa02b49b066d479cb43f7c47e1b494")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

