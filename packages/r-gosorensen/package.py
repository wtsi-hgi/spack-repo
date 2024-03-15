# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGosorensen(RPackage):
	"""Statistical inference based on the Sorensen-Dice dissimilarity and the Gene Ontology (GO)

	This package implements inferential methods to compare gene lists in terms of their biological meaning as expressed in the GO. The compared gene lists are characterized by cross-tabulation frequency tables of enriched GO items. Dissimilarity between gene lists is evaluated using the Sorensen-Dice index. The fundamental guiding principle is that two gene lists are taken as similar if they share a great proportion of common enriched GO items.
	"""
	
	bioc = "goSorensen" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/goSorensen_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/goSorensen/goSorensen_1.4.0.tar.gz"]

	version("1.4.0", md5="8fa5cc982341291dd857ab340abe4c73")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-goprofiles", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
