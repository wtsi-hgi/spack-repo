# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRta10transcriptclusterDb(RPackage):
	"""Affymetrix rta10 annotation data (chip rta10transcriptcluster)

	Affymetrix rta10 annotation data (chip rta10transcriptcluster) assembled using data from public repositories
	"""
	
	bioc = "rta10transcriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rta10transcriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rta10transcriptcluster.db/rta10transcriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="14ade3f4fca2d1091ccb28e7a777f3e5")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

