# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR10kcodDb(RPackage):
	"""Codelink UniSet Rat I Bioarray (~10 000 rat gene targets) annotation data (chip r10kcod)

	Codelink UniSet Rat I Bioarray (~10 000 rat gene targets) annotation data (chip r10kcod) assembled using data from public repositories
	"""
	
	bioc = "r10kcod.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/r10kcod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/r10kcod.db/r10kcod.db_3.4.0.tar.gz"]

	version("3.4.0", md5="4a7a25fee64294cfb5adccaa6cf28772")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.2.1:", type=("build", "run"))

