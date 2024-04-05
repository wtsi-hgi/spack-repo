# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene21sttranscriptclusterDb(RPackage):
	"""Affymetrix hugene21 annotation data (chip hugene21sttranscriptcluster)

	Affymetrix hugene21 annotation data (chip hugene21sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "hugene21sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene21sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene21sttranscriptcluster.db/hugene21sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="ca90de6093bbad760abfcf0cfeada830")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

