# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430bDb(RPackage):
	"""Affymetrix Affymetrix HT_MG-430B Array annotation data (chip htmg430b)

	Affymetrix Affymetrix HT_MG-430B Array annotation data (chip htmg430b) assembled using data from public repositories
	"""
	
	bioc = "htmg430b.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htmg430b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htmg430b.db/htmg430b.db_3.13.0.tar.gz"]

	version("3.13.0", md5="70849a636e972a9be604a3320d3bd814")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

