# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicdoc(RPackage):
	"""A/B compartment detection and differential analysis

	HiCDOC normalizes intrachromosomal Hi-C matrices, uses unsupervised learning to predict A/B compartments from multiple replicates, and detects significant compartment changes between experiment conditions. It provides a collection of functions assembled into a pipeline to filter and normalize the data, predict the compartments and visualize the results. It accepts several type of data: tabular `.tsv` files, Cooler `.cool` or `.mcool` files, Juicer `.hic` files or HiC-Pro `.matrix` and `.bed` files.
	"""
	
	homepage = "https://github.com/mzytnicki/HiCDOC"
	bioc = "HiCDOC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HiCDOC_1.4.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HiCDOC/HiCDOC_1.4.1.tar.gz"]

	version("1.10.1", tag="RELEASE_3_21")
	version("1.4.1", sha256="c4464693066728157213072862195133888b311100d830116e69540b1ccd06df")

	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-multihiccompare", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
