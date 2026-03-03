# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMm24kresogenDb(RPackage):
	"""RNG_MRC Mouse Pangenomic 24k Set annotation data (chip mm24kresogen)

	RNG_MRC Mouse Pangenomic 24k Set annotation data (chip mm24kresogen) assembled using data from public repositories
	"""
	
	bioc = "mm24kresogen.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mm24kresogen.db_2.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mm24kresogen.db/mm24kresogen.db_2.5.0.tar.gz"]

	version("2.5.0", md5="437f5d4bc225ee500af1ecc2d4da472b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@2.5:", type=("build", "run"))

