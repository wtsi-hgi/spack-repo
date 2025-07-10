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

	version("3.2.3", sha256="d5d9d89a44ec8d3cd77c43401ba07e499569077b2c1461f42f7a79728b7fc024")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

