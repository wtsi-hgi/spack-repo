# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHguatlas13kDb(RPackage):
	"""Clontech BD Atlas Long Oligos Human 13K annotation data (chip hguatlas13k)

	Clontech BD Atlas Long Oligos Human 13K annotation data (chip hguatlas13k) assembled using data from public repositories
	"""
	
	bioc = "hguatlas13k.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hguatlas13k.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hguatlas13k.db/hguatlas13k.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="20b6913630e17b424a233dd2d4beed6d413047021104e21a3703b5f422effa96")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

