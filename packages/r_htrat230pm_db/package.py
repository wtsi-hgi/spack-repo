# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtrat230pmDb(RPackage):
	"""Affymetrix Affymetrix HT_Rat230_PM Array annotation data (chip htrat230pm)

	Affymetrix Affymetrix HT_Rat230_PM Array annotation data (chip htrat230pm) assembled using data from public repositories
	"""
	
	bioc = "htrat230pm.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htrat230pm.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htrat230pm.db/htrat230pm.db_3.13.0.tar.gz"]

	version("3.13.0", md5="46ed50806c568bf269fe4c51d3df3955")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

