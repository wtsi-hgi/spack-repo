# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgubeta7Db(RPackage):
	"""Unknown annotation data (chip hgubeta7)

	Unknown annotation data (chip hgubeta7) assembled using data from public repositories
	"""
	
	bioc = "hgubeta7.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgubeta7.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgubeta7.db/hgubeta7.db_3.2.3.tar.gz"]

	version("3.2.3", md5="1b8b065f95d2089985f59f22dcabc824")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation