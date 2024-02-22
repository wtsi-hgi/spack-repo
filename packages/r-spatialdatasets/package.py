# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialdatasets(RPackage):
	"""Collection of spatial omics datasets

	This is a collection of publically available spatial omics datasets. Where possible we have curated these datasets as either SpatialExperiments, MoleculeExperiments or CytoImageLists and included annotations of the sample characteristics.
	"""
	
	homepage = "https://github.com/SydneyBioX/SpatialDatasets"
	bioc = "SpatialDatasets" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/SpatialDatasets_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/SpatialDatasets/SpatialDatasets_1.0.0.tar.gz"]

	version("1.0.0", md5="36fd913ef0d7109d0be40afbc1255548")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))

	# experiment