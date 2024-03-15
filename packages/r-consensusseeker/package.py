# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsensusseeker(RPackage):
	"""Detection of consensus regions inside a group of experiences using genomic positions and genomic ranges

	This package compares genomic positions and genomic ranges from multiple experiments to extract common regions. The size of the analyzed region is adjustable as well as the number of experiences in which a feature must be present in a potential region to tag this region as a consensus region.
	"""
	
	homepage = "https://github.com/ArnaudDroitLab/consensusSeekeR"
	bioc = "consensusSeekeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/consensusSeekeR_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/consensusSeekeR/consensusSeekeR_1.30.0.tar.gz"]

	version("1.30.0", md5="e752cec43fa487cd071a27a1f955b17e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
