# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbscleanr(RPackage):
	"""Error correction tool for noisy genotyping by sequencing (GBS) data

	GBScleanR is a package for quality check, filtering, and error correction of genotype data derived from next generation sequcener (NGS) based genotyping platforms. GBScleanR takes Variant Call Format (VCF) file as input. The main function of this package is `estGeno()` which estimates the true genotypes of samples from given read counts for genotype markers using a hidden Markov model with incorporating uneven observation ratio of allelic reads. This implementation gives robust genotype estimation even in noisy genotype data usually observed in Genotyping-By-Sequnencing (GBS) and similar methods, e.g. RADseq. The current implementation accepts genotype data of a diploid population at any generation of multi-parental cross, e.g. biparental F2 from inbred parents, biparental F2 from outbred parents, and 8-way recombinant inbred lines (8-way RILs) which can be refered to as MAGIC population.
	"""
	
	homepage = "https://github.com/tomoyukif/GBScleanR"
	bioc = "GBScleanR"

	version("2.2.0", commit="8528fbe33192e21ef8235e040f3c653e1a064624")
	version("1.6.0", commit="f84906855cdc1a9d80f21d172859865ddc5fd845")

	depends_on("r-seqarray", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
