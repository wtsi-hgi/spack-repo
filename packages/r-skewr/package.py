# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkewr(RPackage):
	"""Visualize Intensities Produced by Illumina's Human Methylation 450k BeadChip

	The skewr package is a tool for visualizing the output of the Illumina Human Methylation 450k BeadChip to aid in quality control. It creates a panel of nine plots. Six of the plots represent the density of either the methylated intensity or the unmethylated intensity given by one of three subsets of the 485,577 total probes. These subsets include Type I-red, Type I-green, and Type II.The remaining three distributions give the density of the Beta-values for these same three subsets. Each of the nine plots optionally displays the distributions of the "rs" SNP probes and the probes associated with imprinted genes as series of 'tick' marks located above the x-axis.
	"""
	
	bioc = "skewr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/skewr_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/skewr/skewr_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="f234edfd4542c04d55c5d86aa5c44cf9d258f3ce051a0f9ab2c86e30de0b6834")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-methylumi", type=("build", "run"))
	depends_on("r-watermelon", type=("build", "run"))
	depends_on("r-mixsmsn", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kmanifest", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-s4vectors@0.19.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
