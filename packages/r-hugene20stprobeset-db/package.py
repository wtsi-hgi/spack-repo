# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHugene20stprobesetDb(RPackage):
	"""Affymetrix hugene20 annotation data (chip hugene20stprobeset)

	Affymetrix hugene20 annotation data (chip hugene20stprobeset) assembled using data from public repositories
	"""
	
	bioc = "hugene20stprobeset.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hugene20stprobeset.db_8.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hugene20stprobeset.db/hugene20stprobeset.db_8.8.0.tar.gz"]

	version("8.8.0", sha256="f94d92780b842dabd7363c20ff028f4f6a58d685c0a9e44458068b2afacf2ebd")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

