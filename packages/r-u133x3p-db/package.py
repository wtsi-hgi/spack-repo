# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RU133x3pDb(RPackage):
	"""Affymetrix Human X3P Array annotation data (chip u133x3p)

	Affymetrix Human X3P Array annotation data (chip u133x3p) assembled using data from public repositories
	"""
	
	bioc = "u133x3p.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/u133x3p.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/u133x3p.db/u133x3p.db_3.2.3.tar.gz"]

	version("3.2.3", md5="1a36a09dc64b94728bf6ac75600b40c6")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation