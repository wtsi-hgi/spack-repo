# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultirnaflow(RPackage):
	"""An R package for analysing RNA-seq raw counts with several biological conditions and different time points

	Our R package MultiRNAflow provides an easy to use unified framework allowing to automatically make both unsupervised and supervised (DE) analysis for datasets with an arbitrary number of biological conditions and time points.  In particular, our code makes a deep downstream analysis of DE information, e.g. identifying temporal patterns across biological conditions and DE genes which are specific to a biological condition for each time.
	"""
	
	homepage = "https://github.com/loubator/MultiRNAflow"
	bioc = "MultiRNAflow" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MultiRNAflow_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MultiRNAflow/MultiRNAflow_1.0.0.tar.gz"]

	version("1.0.0", md5="cefc109896f4cb34b4ee6a09ae966f42")

	depends_on("r-mfuzz@2.58:", type=("build", "run"))
	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biobase@2.54:", type=("build", "run"))
	depends_on("r-complexheatmap@2.14:", type=("build", "run"))
	depends_on("r-deseq2@1.38.1:", type=("build", "run"))
	depends_on("r-factoextra@1.0.7:", type=("build", "run"))
	depends_on("r-factominer@2.6:", type=("build", "run"))
	depends_on("r-ggalluvial@0.12.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggrepel@0.9.2:", type=("build", "run"))
	depends_on("r-ggsci@2.9:", type=("build", "run"))
	depends_on("r-gprofiler2@0.2.1:", type=("build", "run"))
	depends_on("r-plot3d@1.4:", type=("build", "run"))
	depends_on("r-plot3drgl@1.0.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.8:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.36.2:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.28:", type=("build", "run"))
	depends_on("r-upsetr@1.4:", type=("build", "run"))
