# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu95cDb(RPackage):
	"""Affymetrix Affymetrix HG_U95C Array annotation data (chip hgu95c)

	Affymetrix Affymetrix HG_U95C Array annotation data (chip hgu95c) assembled using data from public repositories
	"""
	
	bioc = "hgu95c.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu95c.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu95c.db/hgu95c.db_3.13.0.tar.gz"]

	version("3.13.0", md5="680cdfc3e63853ace2ec47caa00ded36")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

