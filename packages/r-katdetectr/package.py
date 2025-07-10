# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKatdetectr(RPackage):
	"""Detection, Characterization and Visualization of Kataegis in Sequencing Data

	Kataegis refers to the occurrence of regional hypermutation and is a phenomenon observed in a wide range of malignancies. Using changepoint detection katdetectr aims to identify putative kataegis foci from common data-formats housing genomic variants. Katdetectr has shown to be a robust package for the detection, characterization and visualization of kataegis.
	"""
	
	homepage = "https://doi.org/doi:10.18129/B9.bioc.katdetectr"
	bioc = "katdetectr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/katdetectr_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/katdetectr/katdetectr_1.4.0.tar.gz"]

	version("1.4.0", sha256="3f5d04a60a2d8ff0d9db9ebcbc52347dc046ac25f2327eed5c98421bd7c12a44")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel@1.26.2:", type=("build", "run"))
	depends_on("r-changepoint@2.2.3:", type=("build", "run"))
	depends_on("r-changepoint-np@1.0.3:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-genomicranges@1.44:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.28.4:", type=("build", "run"))
	depends_on("r-iranges@2.26:", type=("build", "run"))
	depends_on("r-maftools@2.10.5:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-s4vectors@0.30.2:", type=("build", "run"))
	depends_on("r-tibble@3.1.6:", type=("build", "run"))
	depends_on("r-variantannotation@1.38:", type=("build", "run"))
	depends_on("r-biobase@2.54:", type=("build", "run"))
	depends_on("r-rdpack@2.3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-bsgenome@1.62:", type=("build", "run"))
	depends_on("r-ggtext@0.1.1:", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg19@1.4.3:", type=("build", "run"))
	depends_on("r-bsgenome-hsapiens-ucsc-hg38@1.4.4:", type=("build", "run"))
	depends_on("r-plyranges@1.17:", type=("build", "run"))
