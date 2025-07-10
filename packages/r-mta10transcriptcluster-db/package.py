# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMta10transcriptclusterDb(RPackage):
	"""Affymetrix mta10 annotation data (chip mta10transcriptcluster)

	Affymetrix mta10 annotation data (chip mta10transcriptcluster) assembled using data from public repositories
	"""
	
	bioc = "mta10transcriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mta10transcriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mta10transcriptcluster.db/mta10transcriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="4a706d20cadd02c2364debfa4e28f9fb56571ac6b85802e0a043801c963068c2")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

