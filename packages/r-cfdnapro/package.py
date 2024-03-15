# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfdnapro(RPackage):
	"""cfDNAPro extracts and Visualises biological features from whole genome sequencing data of cell-free DNA

	cfDNA fragments carry important features for building cancer sample classification ML models, such as fragment size, and fragment end motif etc. Analyzing and visualizing fragment size metrics, as well as other biological features in a curated, standardized, scalable, well-documented, and reproducible way might be time intensive. This package intends to resolve these problems and simplify the process. It offers two sets of functions for cfDNA feature characterization and visualization.
	"""
	
	homepage = "https://github.com/hw538/cfDNAPro"
	bioc = "cfDNAPro" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cfDNAPro_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cfDNAPro/cfDNAPro_1.8.0.tar.gz"]

	version("1.8.0", md5="377fb633e850fcef49fbe86f3c4d1505")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-quantmod@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-rsamtools@2.4:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg38", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ncbi-grch38", type=("build", "run"))
