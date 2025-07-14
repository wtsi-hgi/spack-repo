# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayseq(RPackage):
	"""Empirical Bayesian analysis of patterns of differential expression in count data

	This package identifies differential expression in high-throughput 'count' data, such as that derived from next-generation sequencing machines, calculating estimated posterior likelihoods of differential expression (or more complex hypotheses) via empirical Bayesian methods.
	"""
	
	bioc = "baySeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/baySeq_2.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/baySeq/baySeq_2.36.0.tar.gz"]

	version("2.42.0", tag="RELEASE_3_21")
	version("2.36.0", md5="f46b63ebca2bda7c124133149aa7e552")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
