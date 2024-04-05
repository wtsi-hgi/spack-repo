# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu19ksubcDb(RPackage):
	"""Affymetrix Affymetrix Mu19KsubC Array annotation data (chip mu19ksubc)

	Affymetrix Affymetrix Mu19KsubC Array annotation data (chip mu19ksubc) assembled using data from public repositories
	"""
	
	bioc = "mu19ksubc.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu19ksubc.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu19ksubc.db/mu19ksubc.db_3.13.0.tar.gz"]

	version("3.13.0", md5="bef37c9cd01032e9f1fb177a1af8cba4")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

