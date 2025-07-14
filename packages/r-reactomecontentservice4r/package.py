# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomecontentservice4r(RPackage):
	"""Interface for the Reactome Content Service

	Reactome is a free, open-source, open access, curated and peer-reviewed knowledgebase of bio-molecular pathways. This package is to interact with the Reactome Content Service API. Pre-built functions would allow users to retrieve data and images that consist of proteins, pathways, and other molecules related to a specific gene or entity in Reactome.
	"""
	
	homepage = "https://github.com/reactome/ReactomeContentService4R"
	bioc = "ReactomeContentService4R" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ReactomeContentService4R_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ReactomeContentService4R/ReactomeContentService4R_1.10.0.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.0", sha256="909f782300f11131722a4a7394281468f72d0888fc334c377e592c0c2f11966d")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magick@2.5.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
