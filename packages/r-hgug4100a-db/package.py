# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgug4100aDb(RPackage):
	"""Agilent Human 1 cDNA Microarray Kit annotation data (chip hgug4100a)

	Agilent Human 1 cDNA Microarray Kit annotation data (chip hgug4100a) assembled using data from public repositories
	"""
	
	bioc = "hgug4100a.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hgug4100a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hgug4100a.db/hgug4100a.db_3.2.3.tar.gz"]

	version("3.2.3", md5="b7856928278a77d71f963410ea4f2376")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

	# annotation