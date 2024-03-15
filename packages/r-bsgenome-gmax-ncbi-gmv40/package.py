# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeGmaxNcbiGmv40(RPackage):
	"""Full genome sequences for Glycine max (Gmv40)

	Full genome sequences for Glycine max as provided by NCBI (assembly Glycine_max_v4.0, assembly accession GCF_000004515.5) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Gmax.NCBI.Gmv40" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Gmax.NCBI.Gmv40_4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Gmax.NCBI.Gmv40/BSgenome.Gmax.NCBI.Gmv40_4.0.tar.gz"]

	version("4.0", md5="421c045b993b2cfbc2b08c8103835c56", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Gmax.NCBI.Gmv40_4.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

	# annotation