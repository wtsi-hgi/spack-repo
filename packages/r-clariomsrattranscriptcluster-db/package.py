# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomsrattranscriptclusterDb(RPackage):
	"""Affymetrix clariomsrat annotation data (chip clariomsrattranscriptcluster)

	Affymetrix clariomsrat annotation data (chip clariomsrattranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "clariomsrattranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/clariomsrattranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/clariomsrattranscriptcluster.db/clariomsrattranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="72923a3a90f2df27a361b1730cfc0d00")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation