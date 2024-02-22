# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedtcgadata(RPackage):
	"""Curated Data From The Cancer Genome Atlas (TCGA) as MultiAssayExperiment Objects

	This package provides publicly available data from The Cancer Genome Atlas (TCGA) as MultiAssayExperiment objects. MultiAssayExperiment integrates multiple assays (e.g., RNA-seq, copy number, mutation, microRNA, protein, and others) with clinical / pathological data. It also links assay barcodes with patient identifiers, enabling harmonized subsetting of rows (features) and columns (patients / samples) across the entire multi-'omics experiment.
	"""
	
	bioc = "curatedTCGAData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/curatedTCGAData_1.24.1.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/curatedTCGAData/curatedTCGAData_1.24.1.tar.gz"]

	version("1.24.1", md5="69e06f23ff43332c06bad9bea52b30c9")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment