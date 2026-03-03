# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHta20probesetDb(RPackage):
	"""Affymetrix hta20 annotation data (chip hta20probeset)

	Affymetrix hta20 annotation data (chip hta20probeset) assembled using data from public repositories
	"""
	
	bioc = "hta20probeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hta20probeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hta20probeset.db/hta20probeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="8cc15bb71f3c2776015e55a2d7df2c2f")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

