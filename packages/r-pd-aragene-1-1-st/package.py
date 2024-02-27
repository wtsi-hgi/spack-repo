# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdAragene11St(RPackage):
	"""Platform Design Info for Affymetrix AraGene-1_1-st

	Platform Design Info for Affymetrix AraGene-1_1-st
	"""
	
	bioc = "pd.aragene.1.1.st" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.aragene.1.1.st_3.12.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/pd.aragene.1.1.st/pd.aragene.1.1.st_3.12.0.tar.gz"]

	version("3.12.0", md5="828ad790eb2495e396d7fcd9bcbf9133")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

	# annotation