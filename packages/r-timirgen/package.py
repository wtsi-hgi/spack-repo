# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimirgen(RPackage):
	"""Time sensitive microRNA-mRNA integration, analysis and network generation tool

	TimiRGeN (Time Incorporated miR-mRNA Generation of Networks) is a novel R package which functionally analyses and integrates time course miRNA-mRNA differential expression data. This tool can generate small networks within R or export results into cytoscape or pathvisio for more detailed network construction and hypothesis generation. This tool is created for researchers that wish to dive deep into time series multi-omic datasets. TimiRGeN goes further than many other tools in terms of data reduction. Here, potentially hundreds-of-thousands of potential miRNA-mRNA interactions can be whittled down into a handful of high confidence miRNA-mRNA interactions affecting a signalling pathway, across a time course.
	"""
	
	homepage = "https://github.com/Krutik6/TimiRGeN/"
	bioc = "TimiRGeN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TimiRGeN_1.11.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TimiRGeN/TimiRGeN_1.11.0.tar.gz"]

	version("1.11.0", sha256="22bf75a246dcb1dc85830bdeb9300b00647ae91fe5647d37a6d3d5405b1e9280")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mfuzz", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-dplyr@0.8.4:", type=("build", "run"))
	depends_on("r-freqprof", type=("build", "run"))
	depends_on("r-gtools@3.8.1:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-gghighlight", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph@1.2.4.2:", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rwikipathways", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
