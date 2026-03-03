# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdMirna31(RPackage):
	"""Platform Design Info for Affymetrix miRNA-3_1

	Platform Design Info for Affymetrix miRNA-3_1
	"""
	
	bioc = "pd.mirna.3.1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.mirna.3.1_3.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.mirna.3.1/pd.mirna.3.1_3.8.1.tar.gz"]

	version("3.8.1", md5="296b3584ee5e9416c9018353d3e29c6c", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.mirna.3.1_3.8.1.tar.gz")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rsqlite@0.11.1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.19.41:", type=("build", "run"))
	depends_on("r-oligo@1.21.5:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings@2.25.12:", type=("build", "run"))
	depends_on("r-iranges@1.15.43:", type=("build", "run"))

