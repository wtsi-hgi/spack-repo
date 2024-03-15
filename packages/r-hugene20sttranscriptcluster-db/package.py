# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene20sttranscriptclusterDb(RPackage):
	"""Affymetrix hugene20 annotation data (chip hugene20sttranscriptcluster)

	Affymetrix hugene20 annotation data (chip hugene20sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "hugene20sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene20sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene20sttranscriptcluster.db/hugene20sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="0b929a3a959662e8a7265f58b81b4e35")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation