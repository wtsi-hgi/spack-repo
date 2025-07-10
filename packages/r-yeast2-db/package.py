# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeast2Db(RPackage):
	"""Affymetrix Affymetrix Yeast_2 Array annotation data (chip yeast2)

	Affymetrix Affymetrix Yeast_2 Array annotation data (chip yeast2) assembled using data from public repositories
	"""
	
	bioc = "yeast2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/yeast2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/yeast2.db/yeast2.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="46dff01a289182695d020008cc7328658514de7e67faf7bc354c0f67eed00b2b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-sc-sgd-db@3.13:", type=("build", "run"))

