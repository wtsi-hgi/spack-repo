# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrosophila2Db(RPackage):
	"""Affymetrix Affymetrix Drosophila_2 Array annotation data (chip drosophila2)

	Affymetrix Affymetrix Drosophila_2 Array annotation data (chip drosophila2) assembled using data from public repositories
	"""
	
	bioc = "drosophila2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/drosophila2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/drosophila2.db/drosophila2.db_3.13.0.tar.gz"]

	version("3.13.0", md5="c01d0d1b5e17c3b36ad801b44da72b96")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-dm-eg-db@3.13:", type=("build", "run"))

	# annotation