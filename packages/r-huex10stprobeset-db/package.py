# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuex10stprobesetDb(RPackage):
	"""Affymetrix huex10 annotation data (chip huex10stprobeset)

	Affymetrix huex10 annotation data (chip huex10stprobeset) assembled using data from public repositories
	"""
	
	bioc = "huex10stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/huex10stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/huex10stprobeset.db/huex10stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="2ed209382bca16d8f0999864205e7d0654fe9f2e80f70fe190d0128b0a3c8f20")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

