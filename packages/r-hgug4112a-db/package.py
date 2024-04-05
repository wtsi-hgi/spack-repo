# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgug4112aDb(RPackage):
	"""Agilent "Human Genome, Whole" annotation data (chip hgug4112a)

	Agilent "Human Genome, Whole" annotation data (chip hgug4112a) assembled using data from public repositories
	"""
	
	bioc = "hgug4112a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgug4112a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgug4112a.db/hgug4112a.db_3.2.3.tar.gz"]

	version("3.2.3", md5="67ecf8c887e2ebe1941cc51d0f5fb468")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

