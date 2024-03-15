# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLapointeDb(RPackage):
	"""A package containing metadata for LAPOINTE arrays

	A package containing metadata for LAPOINTE arrays assembled using data from public repositories
	"""
	
	bioc = "LAPOINTE.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/LAPOINTE.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/LAPOINTE.db/LAPOINTE.db_3.2.3.tar.gz"]

	version("3.2.3", md5="434b25ad7411201d8be6bb1a0463b387")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation