# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnMops(RPackage):
	"""cn.mops - Mixture of Poissons for CNV detection in NGS data

	cn.mops (Copy Number estimation by a Mixture Of PoissonS) is a data processing pipeline for copy number variations and aberrations (CNVs and CNAs) from next generation sequencing (NGS) data. The package supplies functions to convert BAM files into read count matrices or genomic ranges objects, which are the input objects for cn.mops. cn.mops models the depths of coverage across samples at each genomic position. Therefore, it does not suffer from read count biases along chromosomes. Using a Bayesian approach, cn.mops decomposes read variations across samples into integer copy numbers and noise by its mixture components and Poisson distributions, respectively. cn.mops guarantees a low FDR because wrong detections are indicated by high noise and filtered out. cn.mops is very fast and written in C++.
	"""
	
	homepage = "http://www.bioinf.jku.at/software/cnmops/cnmops.html"
	bioc = "cn.mops" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cn.mops_1.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cn.mops/cn.mops_1.48.0.tar.gz"]

	version("1.48.0", md5="e4e51a7ecd3810464be443ba9a6b6919")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-exomecopy", type=("build", "run"))
