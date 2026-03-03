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

	version("1.6.0", md5="10ef702e87a5f0517e59c1ccb96b08dc")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
