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

	version("1.54.0", commit="e09a8be4b32b30b024c9b2c4c05981698e288330")
	version("1.48.0", commit="f3cf243d115c4eda23f4396a3093d9d8cd9f5a9d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-exomecopy", type=("build", "run"))
