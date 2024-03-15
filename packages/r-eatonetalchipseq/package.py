# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REatonetalchipseq(RPackage):
	"""ChIP-seq data of ORC-binding sites in Yeast excerpted from Eaton et al. 2010

	ChIP-seq analysis subset from "Conserved nucleosome positioning defines replication origins" (PMID 20351051)
	"""
	
	bioc = "EatonEtAlChIPseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/EatonEtAlChIPseq_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/EatonEtAlChIPseq/EatonEtAlChIPseq_0.40.0.tar.gz"]

	version("0.40.0", md5="e7695c3761d5f3d41dec21b0c8b50947")

	depends_on("r-genomicranges@1.5.42:", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))

	# experiment