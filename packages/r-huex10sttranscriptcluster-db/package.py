# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuex10sttranscriptclusterDb(RPackage):
	"""Affymetrix huex10 annotation data (chip huex10sttranscriptcluster)

	Affymetrix huex10 annotation data (chip huex10sttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "huex10sttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/huex10sttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/huex10sttranscriptcluster.db/huex10sttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="0789a1e8ee4474bd64c2772eab0db247")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

