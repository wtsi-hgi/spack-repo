# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoiseq(RPackage):
	"""Exploratory analysis and differential expression for RNA-seq data

	Analysis of RNA-seq expression data or other similar kind of data. Exploratory plots to evualuate saturation, count distribution, expression per chromosome, type of detected features, features length, etc. Differential expression between two experimental conditions with no parametric assumptions.
	"""
	
	bioc = "NOISeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NOISeq_2.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NOISeq/NOISeq_2.46.0.tar.gz"]

	version("2.46.0", md5="e7ea859871f96aa68269efa3a1e7dd46")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase@2.13.11:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
