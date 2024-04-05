# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmg430pmDb(RPackage):
	"""Affymetrix Affymetrix HT_MG-430_PM Array annotation data (chip htmg430pm)

	Affymetrix Affymetrix HT_MG-430_PM Array annotation data (chip htmg430pm) assembled using data from public repositories
	"""
	
	bioc = "htmg430pm.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htmg430pm.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htmg430pm.db/htmg430pm.db_3.13.0.tar.gz"]

	version("3.13.0", md5="f89738ce2e33d1c626aa2d15cd28a49b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

