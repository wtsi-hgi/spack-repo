# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu11ksubaDb(RPackage):
	"""Affymetrix Affymetrix Mu11KsubA Array annotation data (chip mu11ksuba)

	Affymetrix Affymetrix Mu11KsubA Array annotation data (chip mu11ksuba) assembled using data from public repositories
	"""
	
	bioc = "mu11ksuba.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mu11ksuba.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mu11ksuba.db/mu11ksuba.db_3.13.0.tar.gz"]

	version("3.13.0", md5="73d80611d1eaf8ee1eb37ebc469d97e9")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

	# annotation