# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdinfobuilder(RPackage):
	"""Platform Design Information Package Builder

	Builds platform design information packages. These consist of a SQLite database containing feature-level data such as x, y position on chip and featureSet ID. The database also incorporates featureSet-level annotation data. The products of this packages are used by the oligo pkg.
	"""
	
	bioc = "pdInfoBuilder" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pdInfoBuilder_1.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pdInfoBuilder/pdInfoBuilder_1.66.0.tar.gz"]

	version("1.66.0", sha256="9a257659795ee6a120d2f3a01aa7ac2458b43f99b962a77c67ad556c9e6995ad")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase@2.27.3:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-affxparser@1.39.4:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-biocgenerics@0.13.11:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))
