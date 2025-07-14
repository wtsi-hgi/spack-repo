# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMudata(RPackage):
	"""Serialization for MultiAssayExperiment Objects

	Save MultiAssayExperiments to h5mu files supported by muon and mudata. Muon is a Python framework for multimodal omics data analysis. It uses an HDF5-based format for data storage.
	"""
	
	homepage = "https://github.com/ilia-kats/MuData"
	bioc = "MuData" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MuData_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MuData/MuData_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="5d43b15ec405c0bc3cc1a328773fd76fda63f51555ec57ca10bafaec79dc2e3a")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
