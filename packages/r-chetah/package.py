# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChetah(RPackage):
	"""Fast and accurate scRNA-seq cell type identification

	CHETAH (CHaracterization of cEll Types Aided by Hierarchical classification) is an accurate, selective and fast scRNA-seq classifier. Classification is guided by a reference dataset, preferentially also a scRNA-seq dataset. By hierarchical clustering of the reference data, CHETAH creates a classification tree that enables a step-wise, top-to-bottom classification. Using a novel stopping rule, CHETAH classifies the input cells to the cell types of the references and to "intermediate types": more general classifications that ended in an intermediate node of the tree.
	"""
	
	homepage = "https://github.com/jdekanter/CHETAH"
	bioc = "CHETAH" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CHETAH_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CHETAH/CHETAH_1.18.0.tar.gz"]

	version("1.18.0", sha256="46970b6775d218fdd2e1248f24ae8f24e9f18703c768461c123c4a7dc27ce678")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-biodist", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
