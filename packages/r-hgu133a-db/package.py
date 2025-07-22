# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133aDb(RPackage):
	"""Affymetrix Affymetrix HG-U133A Array annotation data (chip hgu133a)

	Affymetrix Affymetrix HG-U133A Array annotation data (chip hgu133a) assembled using data from public repositories
	"""
	
	bioc = "hgu133a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133a.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133a.db/hgu133a.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="945e21ba79483ef0d022855978b3e46a3cf8f2b27eeb0e93a6c104ed6c7c4c02")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

