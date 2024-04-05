# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgfocusDb(RPackage):
	"""Affymetrix Affymetrix HG-Focus Array annotation data (chip hgfocus)

	Affymetrix Affymetrix HG-Focus Array annotation data (chip hgfocus) assembled using data from public repositories
	"""
	
	bioc = "hgfocus.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgfocus.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgfocus.db/hgfocus.db_3.13.0.tar.gz"]

	version("3.13.0", md5="a6bee48c0aa947d3c7d25ef2c5a4d485")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

