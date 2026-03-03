# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMumosa(RPackage):
	"""Multi-Modal Single-Cell Analysis Methods

	Assorted utilities for multi-modal analyses of single-cell datasets. Includes functions to combine multiple modalities for downstream analysis, perform MNN-based batch correction across multiple modalities, and to compute correlations between assay values for different modalities.
	"""
	
	homepage = "http://bioconductor.org/packages/mumosa"
	bioc = "mumosa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mumosa_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mumosa/mumosa_1.10.0.tar.gz"]

	version("1.10.0", md5="634ea9c4fce9573e5da8297886d4b699")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-scaledmatrix", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-metapod", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-batchelor", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
