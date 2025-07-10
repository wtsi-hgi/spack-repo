# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHs6ug171Db(RPackage):
	"""A package containing metadata for Hs6UG171 arrays

	A package containing metadata for Hs6UG171 arrays assembled using data from public repositories
	"""
	
	bioc = "Hs6UG171.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Hs6UG171.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/Hs6UG171.db/Hs6UG171.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="6aa4fc7d3ef2023f834e34bdee6ffdd6b10720a288ae7bea4a1279387c538a0c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

