# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedbarrayv9Db(RPackage):
	"""FHCRC Nelson Lab pedbarrayv9 Annotation Data (pedbarrayv9)

	FHCRC Nelson Lab pedbarrayv9 Annotation Data (pedbarrayv9) assembled using data from public repositories
	"""
	
	bioc = "pedbarrayv9.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pedbarrayv9.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pedbarrayv9.db/pedbarrayv9.db_3.2.3.tar.gz"]

	version("3.2.3", md5="da4b2f9c0a672e0c9ee53f017bacaff7")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

