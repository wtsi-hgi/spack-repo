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

    version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="2f0f4845e0e5a25a1cf14c7209b833e85d0541f8f9986978c2946e2f0bed86d5")

	depends_on("r@2.10:", type=("build", "run"))
