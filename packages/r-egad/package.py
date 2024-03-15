# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgad(RPackage):
	"""Extending guilt by association by degree

	The package implements a series of highly efficient tools to calculate functional properties of networks based on guilt by association methods.
	"""
	
	bioc = "EGAD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EGAD_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EGAD/EGAD_1.30.0.tar.gz"]

	version("1.30.0", md5="9a76ae26d942a1e8b8c8764b80c69927")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
