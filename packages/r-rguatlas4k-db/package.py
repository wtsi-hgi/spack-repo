# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRguatlas4kDb(RPackage):
	"""Clontech BD Atlas Long Oligos Rat 4K annotation data (chip rguatlas4k)

	Clontech BD Atlas Long Oligos Rat 4K annotation data (chip rguatlas4k) assembled using data from public repositories
	"""
	
	bioc = "rguatlas4k.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rguatlas4k.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rguatlas4k.db/rguatlas4k.db_3.2.3.tar.gz"]

	version("3.2.3", md5="6a360676e08319ec5465c47c758110bd")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.3:", type=("build", "run"))

	# annotation