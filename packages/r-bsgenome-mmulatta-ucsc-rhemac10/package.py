# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmulattaUcscRhemac10(RPackage):
	"""Full genome sequences for Macaca mulatta (UCSC version rheMac10)

	Full genome sequences for Macaca mulatta (Rhesus) as provided by UCSC (rheMac10, Feb. 2019) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mmulatta.UCSC.rheMac10" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac10_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmulatta.UCSC.rheMac10/BSgenome.Mmulatta.UCSC.rheMac10_1.4.2.tar.gz"]

	version("1.4.2", md5="2f2afe40d5dcf8d8620aa5e12e311fbc", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac10_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation