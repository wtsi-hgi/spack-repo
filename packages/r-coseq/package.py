# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoseq(RPackage):
	"""Co-Expression Analysis of Sequencing Data

	Co-expression analysis for expression profiles arising from high-throughput sequencing data. Feature (e.g., gene) profiles are clustered using adapted transformations and mixture models or a K-means algorithm, and model selection criteria (to choose an appropriate number of clusters) are provided.
	"""
	
	bioc = "coseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/coseq_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/coseq/coseq_1.26.0.tar.gz"]

	version("1.32.1", tag="RELEASE_3_21")
	version("1.26.0", sha256="a83d149e511b5aa3303cd49e5eb37175862828e5c0a376db1facbfe9ff0205b9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-rmixmod", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-htsfilter", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-htscluster", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
