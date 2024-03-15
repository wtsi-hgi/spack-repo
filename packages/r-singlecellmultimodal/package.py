# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglecellmultimodal(RPackage):
	"""Integrating Multi-modal Single Cell Experiment datasets

	SingleCellMultiModal is an ExperimentHub package that serves multiple datasets obtained from GEO and other sources and represents them as MultiAssayExperiment objects. We provide several multi-modal datasets including scNMT, 10X Multiome, seqFISH, CITEseq, SCoPE2, and others. The scope of the package is is to provide data for benchmarking and analysis.
	"""
	
	bioc = "SingleCellMultiModal" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SingleCellMultiModal_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SingleCellMultiModal/SingleCellMultiModal_1.14.0.tar.gz"]

	version("1.14.0", md5="e397bc4fbd9ea63f6660758f01d01d38")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocbaseutils", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

	# experiment