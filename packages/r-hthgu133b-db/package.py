# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHthgu133bDb(RPackage):
	"""Affymetrix Affymetrix HT_HG-U133B Array annotation data (chip hthgu133b)

	Affymetrix Affymetrix HT_HG-U133B Array annotation data (chip hthgu133b) assembled using data from public repositories
	"""
	
	bioc = "hthgu133b.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hthgu133b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hthgu133b.db/hthgu133b.db_3.13.0.tar.gz"]

	version("3.13.0", md5="8501401a7385e28173ea7b60aa3bf3d2")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation