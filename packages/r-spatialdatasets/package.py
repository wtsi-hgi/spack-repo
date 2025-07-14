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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SpatialDatasets_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SpatialDatasets/SpatialDatasets_1.0.0.tar.gz"]

    version("1.6.3", tag="RELEASE_3_21")
	version("1.0.0", sha256="febdafeb1b405ba97eadf6f2de0dc4e82f796667fdd51249e6ba805efd7bfaeb")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))

