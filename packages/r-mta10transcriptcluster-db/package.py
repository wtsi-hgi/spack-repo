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

	version("8.8.0", md5="bfd13b16b71ac2cfc82f40f2d102892b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation