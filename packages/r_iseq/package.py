# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseq(RPackage):
	"""Bayesian Hierarchical Modeling of ChIP-seq Data Through Hidden Ising Models

	Bayesian hidden Ising models are implemented to identify IP-enriched genomic regions from ChIP-seq data. They can be used to analyze ChIP-seq data with and without controls and replicates.
	"""
	
	bioc = "iSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iSeq_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iSeq/iSeq_1.54.0.tar.gz"]

	version("1.54.0", md5="1798c4c248175516afc66ee7f45d5051")

	depends_on("r@2.10:", type=("build", "run"))
