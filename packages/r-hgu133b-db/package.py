# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133bDb(RPackage):
	"""Affymetrix Affymetrix HG-U133B Array annotation data (chip hgu133b)

	Affymetrix Affymetrix HG-U133B Array annotation data (chip hgu133b) assembled using data from public repositories
	"""
	
	bioc = "hgu133b.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133b.db/hgu133b.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="1dacdd746b1131ae9966df75e0dbae7ece769fa5c2acaa72e750e119f8281770")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

