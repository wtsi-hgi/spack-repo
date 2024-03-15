# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu11ksubbDb(RPackage):
	"""Affymetrix Affymetrix Mu11KsubB Array annotation data (chip mu11ksubb)

	Affymetrix Affymetrix Mu11KsubB Array annotation data (chip mu11ksubb) assembled using data from public repositories
	"""
	
	bioc = "mu11ksubb.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu11ksubb.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu11ksubb.db/mu11ksubb.db_3.13.0.tar.gz"]

	version("3.13.0", md5="2b61d911c3595843e80041949cb79b41")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation