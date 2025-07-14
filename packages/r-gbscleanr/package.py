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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GBScleanR_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GBScleanR/GBScleanR_1.6.0.tar.gz"]

	version("2.2.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="c74244d165f7bda53f0adc0ae5a128b22d8f5574eb900e0e0b0180861ce163a7")

	depends_on("r-seqarray", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
