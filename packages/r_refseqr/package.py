# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefseqr(RPackage):
	"""Common Computational Operations Working with RefSeq Entries
(GenBank)

	Fetches NCBI data (RefSeq <https://www.ncbi.nlm.nih.gov/refseq/> database) and provides an environment to  
    extract information at the level of gene, mRNA or protein accessions. 
	"""
	
	homepage = "https://github.com/jdieramon/refseqR"
	cran = "refseqR" 

	version("1.0.1", md5="bf6ce34c1c87f260aeb5633fcff21b38")

	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
