# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene20sttranscriptclusterDb(RPackage):
	"""Affymetrix mogene20 annotation data (chip mogene20sttranscriptcluster)

	Affymetrix mogene20 annotation data (chip mogene20sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "mogene20sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene20sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene20sttranscriptcluster.db/mogene20sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="4ff574cf4943a9c176d703fc9772f8669a6198cd06e6850d3fcc4595d4baffae")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

