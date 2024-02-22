# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrugtargetinteractions(RPackage):
	"""Drug-Target Interactions

	Provides utilities for identifying drug-target interactions for sets of small molecule or gene/protein identifiers. The required drug-target interaction information is obained from a local SQLite instance of the ChEMBL database. ChEMBL has been chosen for this purpose, because it provides one of the most comprehensive and best annotatated knowledge resources for drug-target information available in the public domain.
	"""
	
	homepage = "https://github.com/girke-lab/drugTargetInteractions"
	bioc = "drugTargetInteractions" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/drugTargetInteractions_1.10.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/drugTargetInteractions/drugTargetInteractions_1.10.1.tar.gz"]

	version("1.10.1", md5="c1a702c085df262e0a697b6687ea3ee4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-uniprot-ws", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
