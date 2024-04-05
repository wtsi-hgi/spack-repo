# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene21sttranscriptclusterDb(RPackage):
	"""Affymetrix mogene21 annotation data (chip mogene21sttranscriptcluster)

	Affymetrix mogene21 annotation data (chip mogene21sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "mogene21sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mogene21sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mogene21sttranscriptcluster.db/mogene21sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="10aaecc97bf06bfe770496b99612837a")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

