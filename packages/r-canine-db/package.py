# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanineDb(RPackage):
	"""Affymetrix Affymetrix Canine Array annotation data (chip canine)

	Affymetrix Affymetrix Canine Array annotation data (chip canine) assembled using data from public repositories
	"""
	
	bioc = "canine.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/canine.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/canine.db/canine.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="7a58348cb577257a211445980b25629d189f787c1c6745d92c54647301a435f4")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-cf-eg-db@3.13:", type=("build", "run"))

