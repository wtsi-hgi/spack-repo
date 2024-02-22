# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScds(RPackage):
	"""In-Silico Annotation of Doublets for Single Cell RNA Sequencing Data

	In single cell RNA sequencing (scRNA-seq) data combinations of cells are sometimes considered a single cell (doublets). The scds package provides methods to annotate doublets in scRNA-seq data computationally.
	"""
	
	bioc = "scds" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scds_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scds/scds_1.18.0.tar.gz"]

	version("1.18.0", md5="df6bd91f4acdd6ea2e54d2f20f632cbf")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
