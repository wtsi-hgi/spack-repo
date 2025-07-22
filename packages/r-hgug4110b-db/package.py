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

	version("3.2.3", sha256="9eb92d603195d12782ffc8668738c1f0dc047028bb56593355c9d1d98c8ff162")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

