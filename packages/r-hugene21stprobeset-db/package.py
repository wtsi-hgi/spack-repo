# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene21stprobesetDb(RPackage):
	"""Affymetrix hugene21 annotation data (chip hugene21stprobeset)

	Affymetrix hugene21 annotation data (chip hugene21stprobeset) assembled using data from public repositories
	"""
	
	bioc = "hugene21stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene21stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene21stprobeset.db/hugene21stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", md5="2b816dca48d0b2e1a946469b8d85d257")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation