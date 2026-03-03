# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetdx(RPackage):
	"""Network-based patient classifier

	netDx is a general-purpose algorithm to build a patient classifier from heterogenous patient data. The method converts data into patient similarity networks at the level of features. Feature selection identifies features of predictive value to each class. Methods are provided for versatile predictor design and performance evaluation using standard measures. netDx natively groups molecular data into pathway-level features and connects with Cytoscape for network visualization of pathway themes. For method details see: Pai et al. (2019). netDx: interpretable patient classification using integrated patient similarity networks. Molecular Systems Biology. 15, e8497
	"""
	
	homepage = "http://netdx.org"
	bioc = "netDx" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/netDx_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/netDx/netDx_1.14.0.tar.gz"]

	version("1.14.0", md5="6fdc48ce518c74e0261acee84948ce26")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
