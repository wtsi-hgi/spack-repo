# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlseq(RPackage):
	"""Machine Learning Interface for RNA-Seq Data

	This package applies several machine learning methods, including SVM, bagSVM, Random Forest and CART to RNA-Seq data.
	"""
	
	bioc = "MLSeq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MLSeq_2.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MLSeq/MLSeq_2.20.0.tar.gz"]

	version("2.20.0", md5="07ebcff7e7a474bc21b783a6ebc2605b")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-pamr", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-sseq", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
