# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChickenDb(RPackage):
	"""Affymetrix Affymetrix Chicken Array annotation data (chip chicken)

	Affymetrix Affymetrix Chicken Array annotation data (chip chicken) assembled using data from public repositories
	"""
	
	bioc = "chicken.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/chicken.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/chicken.db/chicken.db_3.13.0.tar.gz"]

	version("3.13.0", md5="512f887df339529d4883aad3f3eb6fb8")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-gg-eg-db@3.13:", type=("build", "run"))

	# annotation