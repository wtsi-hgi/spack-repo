# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmulattaUcscRhemac8(RPackage):
	"""Full genome sequences for Macaca mulatta (UCSC version rheMac8)

	Full genome sequences for Macaca mulatta (Rhesus) as provided by UCSC (rheMac8, Nov. 2015) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mmulatta.UCSC.rheMac8" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac8_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmulatta.UCSC.rheMac8/BSgenome.Mmulatta.UCSC.rheMac8_1.4.2.tar.gz"]

	version("1.4.2", md5="e9ad1f70f652c62554e2c5af7638c015", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac8_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation