# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasic4cseq(RPackage):
	"""Basic4Cseq: an R/Bioconductor package for analyzing 4C-seq data

	Basic4Cseq is an R/Bioconductor package for basic filtering, analysis and subsequent visualization of 4C-seq data. Virtual fragment libraries can be created for any BSGenome package, and filter functions for both reads and fragments and basic quality controls are included. Fragment data in the vicinity of the experiment's viewpoint can be visualized as a coverage plot based on a running median approach and a multi-scale contact profile.
	"""
	
	bioc = "Basic4Cseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Basic4Cseq_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Basic4Cseq/Basic4Cseq_1.38.0.tar.gz"]

	version("1.38.0", sha256="a463cea67c318d6ba1ff19263e57811096949f85088b4a063f871784decc99ee")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcircos", type=("build", "run"))
	depends_on("r-bsgenome-ecoli-ncbi-20080805", type=("build", "run"))
