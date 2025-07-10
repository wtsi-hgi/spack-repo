# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu6800Db(RPackage):
	"""Affymetrix Affymetrix Hu6800 Array annotation data (chip hu6800)

	Affymetrix Affymetrix Hu6800 Array annotation data (chip hu6800) assembled using data from public repositories
	"""
	
	bioc = "hu6800.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu6800.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu6800.db/hu6800.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="90e7806316808ba87b26655218f87cc726289857fc8424b95ae2290aa7190a5e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

