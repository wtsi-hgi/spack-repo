# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133aDb(RPackage):
	"""Affymetrix Affymetrix HT_HG-U133A Array annotation data (chip hthgu133a)

	Affymetrix Affymetrix HT_HG-U133A Array annotation data (chip hthgu133a) assembled using data from public repositories
	"""
	
	bioc = "hthgu133a.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hthgu133a.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hthgu133a.db/hthgu133a.db_3.13.0.tar.gz"]

	version("3.13.0", md5="769ed088760102b61edfb73454d4c642")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation