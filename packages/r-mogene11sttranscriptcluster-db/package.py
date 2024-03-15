# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene11sttranscriptclusterDb(RPackage):
	"""Affymetrix mogene11 annotation data (chip mogene11sttranscriptcluster)

	Affymetrix mogene11 annotation data (chip mogene11sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "mogene11sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene11sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene11sttranscriptcluster.db/mogene11sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="2a3bf07a4794e2349b7d09368dcb7d18")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation