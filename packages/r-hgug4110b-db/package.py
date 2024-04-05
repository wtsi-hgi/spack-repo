# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgug4110bDb(RPackage):
	"""Agilent Human 1A (V2) annotation data (chip hgug4110b)

	Agilent Human 1A (V2) annotation data (chip hgug4110b) assembled using data from public repositories
	"""
	
	bioc = "hgug4110b.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hgug4110b.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hgug4110b.db/hgug4110b.db_3.2.3.tar.gz"]

	version("3.2.3", md5="a9edcdbc121f22d4dec335a64598ff0e")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

