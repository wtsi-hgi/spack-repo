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

	version("3.2.3", sha256="bd57e228a20744ed325b970ddd5ca731ca45e957c39d72eebcd7f2d4b0cc9574")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))

