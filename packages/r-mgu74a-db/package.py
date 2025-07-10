# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgu74aDb(RPackage):
	"""Affymetrix Affymetrix MG_U74A Array annotation data (chip mgu74a)

	Affymetrix Affymetrix MG_U74A Array annotation data (chip mgu74a) assembled using data from public repositories
	"""
	
	bioc = "mgu74a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mgu74a.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mgu74a.db/mgu74a.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="7b0ec5d3407d644a8736a3758a93583f920f7c57d0d4a596eb947907f7f27af6")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

