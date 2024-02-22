# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomsmousehttranscriptclusterDb(RPackage):
	"""Affymetrix clariomsmouseht annotation data (chip clariomsmousehttranscriptcluster)

	Affymetrix clariomsmouseht annotation data (chip clariomsmousehttranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "clariomsmousehttranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/clariomsmousehttranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/clariomsmousehttranscriptcluster.db/clariomsmousehttranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="c0aa96cbd5ee7e19296dde5a72232d17")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation