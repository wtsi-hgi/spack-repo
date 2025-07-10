# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeMmulattaUcscRhemac2(RPackage):
	"""Full genome sequences for Macaca mulatta (UCSC version rheMac2)

	Full genome sequences for Macaca mulatta (Rhesus) as provided by UCSC (rheMac2, Jan. 2006) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Mmulatta.UCSC.rheMac2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac2_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Mmulatta.UCSC.rheMac2/BSgenome.Mmulatta.UCSC.rheMac2_1.4.0.tar.gz"]

	version("1.4.0", sha256="52a6ddb8b280269bff605e7e67c7191fc148599d9f833a5b78471dec42e37a97", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Mmulatta.UCSC.rheMac2_1.4.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

