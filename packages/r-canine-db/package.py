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

	version("3.13.0", md5="a876bb01eda62604a32a96b46e34162b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-cf-eg-db@3.13:", type=("build", "run"))

	# annotation