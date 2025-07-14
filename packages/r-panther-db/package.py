# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPantherDb(RPackage):
	"""A set of annotation maps describing the entire PANTHER Gene Ontology

	A set of annotation maps describing the entire Gene Ontology assembled using data from PANTHER.
	"""
	
	bioc = "PANTHER.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/PANTHER.db_1.0.12.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/PANTHER.db/PANTHER.db_1.0.12.tar.gz"]

	version("1.0.12", tag="RELEASE_3_21")
	version("1.0.12", sha256="186ff9f25e46dce9d7c183f93e96ff0527e3a36515cf09cd8506f5c80e7acd17")

	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-biocfilecache@1.10.1:", type=("build", "run"))

