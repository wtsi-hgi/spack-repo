# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAmelliferaUcscApimel2(RPackage):
	"""Full genome sequences for Apis mellifera (UCSC version apiMel2)

	Full genome sequences for Apis mellifera (Honey Bee) as provided by UCSC (apiMel2, Jan. 2005) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Amellifera.UCSC.apiMel2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Amellifera.UCSC.apiMel2_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Amellifera.UCSC.apiMel2/BSgenome.Amellifera.UCSC.apiMel2_1.4.0.tar.gz"]

	version("1.4.0", md5="436ddf54868906e7d1135369d41a2ffe", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Amellifera.UCSC.apiMel2_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

