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
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgu133b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgu133b.db/hgu133b.db_3.13.0.tar.gz"]

	version("3.13.0", md5="ff7930c99300c1022fde06ebe5c4a8cc")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation