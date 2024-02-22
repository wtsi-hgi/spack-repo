# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZebrafishDb(RPackage):
	"""Affymetrix Affymetrix Zebrafish Array annotation data (chip zebrafish)

	Affymetrix Affymetrix Zebrafish Array annotation data (chip zebrafish) assembled using data from public repositories
	"""
	
	bioc = "zebrafish.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/zebrafish.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/zebrafish.db/zebrafish.db_3.13.0.tar.gz"]

	version("3.13.0", md5="64e40a61e81ac9397affb09880846559")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-dr-eg-db@3.13:", type=("build", "run"))

	# annotation