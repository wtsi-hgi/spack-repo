# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene10sttranscriptclusterDb(RPackage):
	"""Affymetrix hugene10 annotation data (chip hugene10sttranscriptcluster)

	Affymetrix hugene10 annotation data (chip hugene10sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "hugene10sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene10sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene10sttranscriptcluster.db/hugene10sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="a32fb5729d37e96f157b0a1085dff43e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

