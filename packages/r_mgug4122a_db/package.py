# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgug4122aDb(RPackage):
	"""Agilent "Mouse Genome, Whole" annotation data (chip mgug4122a)

	Agilent "Mouse Genome, Whole" annotation data (chip mgug4122a) assembled using data from public repositories
	"""
	
	bioc = "mgug4122a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgug4122a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgug4122a.db/mgug4122a.db_3.2.3.tar.gz"]

	version("3.2.3", md5="5fcdce909ac1c0ccbf06bf6411f6fe52")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))

