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

	version("1.14.0", commit="ba29cd23a160e6c18fed63d7e676452c8e8a19ec")
	version("1.8.0", commit="01178b82ab2becba9cd4905ba50e461f0cda4b1d")

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
