# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListeretalbsseq(RPackage):
	"""BS-seq data of H1 and IMR90 cell line excerpted from Lister et al. 2009

	Base resolution bisulfite sequencing data of Human DNA methylomes
	"""
	
	bioc = "ListerEtAlBSseq" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/ListerEtAlBSseq_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/ListerEtAlBSseq/ListerEtAlBSseq_1.34.0.tar.gz"]

	version("1.34.0", md5="302e026ae021a5f26c149b5086569db1")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-methylpipe", type=("build", "run"))

	# experiment