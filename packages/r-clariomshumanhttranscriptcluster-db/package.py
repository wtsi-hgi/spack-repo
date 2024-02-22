# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomshumanhttranscriptclusterDb(RPackage):
	"""Affymetrix clariomshumanht annotation data (chip clariomshumanhttranscriptcluster)

	Affymetrix clariomshumanht annotation data (chip clariomshumanhttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "clariomshumanhttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/clariomshumanhttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/clariomshumanhttranscriptcluster.db/clariomshumanhttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="6a5e8e1f9768694be99277aafcc0a69a")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation