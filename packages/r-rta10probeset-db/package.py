# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRta10probesetDb(RPackage):
	"""Affymetrix rta10 annotation data (chip rta10probeset)

	Affymetrix rta10 annotation data (chip rta10probeset) assembled using data from public repositories
	"""
	
	bioc = "rta10probeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rta10probeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rta10probeset.db/rta10probeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="ce002623471eef89fb841f0bf3e7c9f8")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

