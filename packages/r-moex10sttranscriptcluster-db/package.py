# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoex10sttranscriptclusterDb(RPackage):
	"""Affymetrix moex10 annotation data (chip moex10sttranscriptcluster)

	Affymetrix moex10 annotation data (chip moex10sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "moex10sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/moex10sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/moex10sttranscriptcluster.db/moex10sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="bc3357b3c77ab7bf1dfb66f5f7da36ec")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

