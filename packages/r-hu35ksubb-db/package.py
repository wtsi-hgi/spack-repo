# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHu35ksubbDb(RPackage):
	"""Affymetrix Affymetrix Hu35KsubB Array annotation data (chip hu35ksubb)

	Affymetrix Affymetrix Hu35KsubB Array annotation data (chip hu35ksubb) assembled using data from public repositories
	"""
	
	bioc = "hu35ksubb.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hu35ksubb.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hu35ksubb.db/hu35ksubb.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="fca91dcfeee603db4bbd667a726447ea2d25b62cffa953a986a840e6b874ef63")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

