# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnprelate(RPackage):
	"""Parallel Computing Toolset for Relatedness and Principal Component
	Analysis of SNP Data.

	Genome-wide association studies (GWAS) are widely used to investigate
	the genetic basis of diseases and traits, but they pose many
	computational challenges. We developed an R package SNPRelate to provide
	a binary format for single-nucleotide polymorphism (SNP) data in GWAS
	utilizing CoreArray Genomic Data Structure (GDS) data files. The GDS
	format offers the efficient operations specifically designed for
	integers with two bits, since a SNP could occupy only two bits.
	SNPRelate is also designed to accelerate two key computations on SNP
	data using parallel computing for multi-core symmetric multiprocessing
	computer architectures: Principal Component Analysis (PCA) and
	relatedness analysis using Identity-By-Descent measures. The SNP GDS
	format is also used by the GWASTools package with the support of S4
	classes and generic functions. The extended GDS format is implemented in
	the SeqArray package to support the storage of single nucleotide
	variations (SNVs), insertion/deletion polymorphism (indel) and
	structural variation calls."""

	bioc = "SNPRelate"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SNPRelate_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SNPRelate/SNPRelate_1.36.0.tar.gz"]

	version("1.36.0", md5="f4e5095c6b99014e02d770e7f4bd5617")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
