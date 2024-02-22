# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClariomshumantranscriptclusterDb(RPackage):
	"""Affymetrix clariomshuman annotation data (chip clariomshumantranscriptcluster)

	Affymetrix clariomshuman annotation data (chip clariomshumantranscriptcluster) assembled using data from public repositories
	"""
	
	bioc = "clariomshumantranscriptcluster.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/clariomshumantranscriptcluster.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/clariomshumantranscriptcluster.db/clariomshumantranscriptcluster.db_8.8.0.tar.gz"]

	version("8.8.0", md5="309b29e044e1227da6d4825bbdf04b76")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation