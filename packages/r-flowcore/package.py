# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowcore(RPackage):
	"""flowCore: Basic structures for flow cytometry data

	Provides S4 data structures and basic functions to deal with flow cytometry data.
	"""
	
	bioc = "flowCore" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowCore_2.14.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowCore/flowCore_2.14.2.tar.gz"]

	version("2.14.2", sha256="454da943873fa90b1da05633ab4bad93a078160948a88783eef4b1edaf6187e0")
	version("2.14.1", md5="29b7b1bbecfbd24824f7ec4334a5e640")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.29.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-cytolib", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-bh@1.81:", type=("build", "run"))
	depends_on("r-rprotobuflib", type=("build", "run"))
