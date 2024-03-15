# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230aDb(RPackage):
	"""Affymetrix Affymetrix RAE230A Array annotation data (chip rae230a)

	Affymetrix Affymetrix RAE230A Array annotation data (chip rae230a) assembled using data from public repositories
	"""
	
	bioc = "rae230a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rae230a.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rae230a.db/rae230a.db_3.13.0.tar.gz"]

	version("3.13.0", md5="a2a80af1669fc038a64effbf5a4b246d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation