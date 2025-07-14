# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabolomicsworkbenchr(RPackage):
	"""Metabolomics Workbench in R

	This package provides functions for interfacing with the Metabolomics Workbench RESTful API. Study, compound, protein and gene information can be searched for using the API. Methods to obtain study data in common Bioconductor formats such as SummarizedExperiment and MultiAssayExperiment are also included.
	"""
	
	bioc = "metabolomicsWorkbenchR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/metabolomicsWorkbenchR_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/metabolomicsWorkbenchR/metabolomicsWorkbenchR_1.12.0.tar.gz"]

    version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="63113b093e79341a6ce74410a9a348fc4ad7d895911d12a70c7b5f78858fecb9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-struct", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
