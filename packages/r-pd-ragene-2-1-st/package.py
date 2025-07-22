# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdRagene21St(RPackage):
	"""Platform Design Info for Affymetrix RaGene-2_1-st

	Platform Design Info for Affymetrix RaGene-2_1-st
	"""
	
	bioc = "pd.ragene.2.1.st" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.ragene.2.1.st_3.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.ragene.2.1.st/pd.ragene.2.1.st_3.14.1.tar.gz"]

	version("3.14.1", sha256="7f6bed6299d2f0a530faf998a23fd4d8b72db15675a3059eb9cf9dc92cc43fcd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

