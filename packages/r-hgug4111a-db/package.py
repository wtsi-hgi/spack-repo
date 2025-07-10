# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgug4111aDb(RPackage):
	"""Agilent Human 1B annotation data (chip hgug4111a)

	Agilent Human 1B annotation data (chip hgug4111a) assembled using data from public repositories
	"""
	
	bioc = "hgug4111a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgug4111a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgug4111a.db/hgug4111a.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="76989507ffbeacb7f5ad479b51390d85b4d8d9c410d0bd9063226191ca49a82d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

