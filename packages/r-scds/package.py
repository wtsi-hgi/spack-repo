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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scds_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scds/scds_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="c0ba79cd36dc4ba825c0f6cc6cf5a76e61d7215c07902bf48732265103dbbf32")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
