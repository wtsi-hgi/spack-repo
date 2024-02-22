# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133plusaDb(RPackage):
	"""Affymetrix Affymetrix HT_HG-U133_Plus_A Array annotation data (chip hthgu133plusa)

	Affymetrix Affymetrix HT_HG-U133_Plus_A Array annotation data (chip hthgu133plusa) assembled using data from public repositories
	"""
	
	bioc = "hthgu133plusa.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hthgu133plusa.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hthgu133plusa.db/hthgu133plusa.db_3.13.0.tar.gz"]

	version("3.13.0", md5="477cb32e1d8eb6da894486ad810b4232")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation