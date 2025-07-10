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

	version("3.4.0", sha256="b55a93f61836caa1363ef45b71de5fe687444111e61a38702c17b386962b6b1c")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.2.1:", type=("build", "run"))

