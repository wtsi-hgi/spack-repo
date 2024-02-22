# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu19ksubbDb(RPackage):
	"""Affymetrix Affymetrix Mu19KsubB Array annotation data (chip mu19ksubb)

	Affymetrix Affymetrix Mu19KsubB Array annotation data (chip mu19ksubb) assembled using data from public repositories
	"""
	
	bioc = "mu19ksubb.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/mu19ksubb.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/mu19ksubb.db/mu19ksubb.db_3.13.0.tar.gz"]

	version("3.13.0", md5="1b177a3b5626c825c91e7c25e0acd897")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation