# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrnaseq(RPackage):
	"""Collection of Public Single-Cell RNA-Seq Datasets

	Gene-level counts for a collection of public scRNA-seq datasets, provided as SingleCellExperiment objects with cell- and gene-level metadata.
	"""
	
	bioc = "scRNAseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/scRNAseq_2.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/scRNAseq/scRNAseq_2.16.0.tar.gz"]

	version("2.22.0", tag="RELEASE_3_21")
	version("2.16.0", sha256="5c2144291969ee9b4c23eb450d0f23c71bbbdc79b868ba8f6b73d283b11e7035")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub@2.3.4:", type=("build", "run"))
	depends_on("r-annotationhub@3.3.6:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))

