# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogene10sttranscriptclusterDb(RPackage):
	"""Affymetrix mogene10 annotation data (chip mogene10sttranscriptcluster)

	Affymetrix mogene10 annotation data (chip mogene10sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "mogene10sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mogene10sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mogene10sttranscriptcluster.db/mogene10sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="9553a8ecefad2baa7241c6b6bb8013f5")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation