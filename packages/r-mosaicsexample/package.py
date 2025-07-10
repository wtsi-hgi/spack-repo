# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMosaicsexample(RPackage):
	"""Example data for the mosaics package, which implements MOSAiCS and MOSAiCS-HMM, a statistical framework to analyze one-sample or two-sample ChIP-seq data for transcription factor binding and histone modification

	Data for the mosaics package, consisting of (1) chromosome 22 ChIP and control sample data from a ChIP-seq experiment of STAT1 binding and H3K4me3 modification in MCF7 cell line from ENCODE database (HG19) and (2) chromosome 21 ChIP and control sample data from a ChIP-seq experiment of STAT1 binding, with mappability, GC content, and sequence ambiguity scores of human genome HG18.
	"""
	
	homepage = "http://groups.google.com/group/mosaics_user_group"
	bioc = "mosaicsExample" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/mosaicsExample_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/mosaicsExample/mosaicsExample_1.40.0.tar.gz"]

	version("1.40.0", sha256="99ccc8a960cca6e2ab2c74869e81979c843e58a5b713cd7b506cd0a2cf3ca90b")

	depends_on("r@2.11.1:", type=("build", "run"))

