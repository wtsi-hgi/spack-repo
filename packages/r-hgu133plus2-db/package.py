# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgu133plus2Db(RPackage):
	"""Affymetrix Affymetrix HG-U133_Plus_2 Array annotation data (chip hgu133plus2)

	Affymetrix Affymetrix HG-U133_Plus_2 Array annotation data (chip hgu133plus2) assembled using data from public repositories
	"""
	
	bioc = "hgu133plus2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgu133plus2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgu133plus2.db/hgu133plus2.db_3.13.0.tar.gz"]

	version("3.13.0", md5="459fcf4880a9eaa25b373c5635fede3d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation