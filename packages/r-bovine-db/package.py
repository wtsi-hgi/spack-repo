# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBovineDb(RPackage):
	"""Affymetrix Affymetrix Bovine Array annotation data (chip bovine)

	Affymetrix Affymetrix Bovine Array annotation data (chip bovine) assembled using data from public repositories
	"""
	
	bioc = "bovine.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/bovine.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/bovine.db/bovine.db_3.13.0.tar.gz"]

	version("3.13.0", md5="dcc1180e8ac11247f9899f140082647e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-bt-eg-db@3.13:", type=("build", "run"))

	# annotation