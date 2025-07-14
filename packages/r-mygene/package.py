# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMygene(RPackage):
	"""Access MyGene.Info_ services

	MyGene.Info_ provides simple-to-use REST web services to query/retrieve gene annotation data. It's designed with simplicity and performance emphasized. *mygene*, is an easy-to-use R wrapper to access MyGene.Info_ services.
	"""
	
	bioc = "mygene" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mygene_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mygene/mygene_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="556e0ef8b75df9dff6ff496280a5dd50a5b5ceb7dab5f247f71e9d7c158312a8")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-httr@0.3:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.7:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
