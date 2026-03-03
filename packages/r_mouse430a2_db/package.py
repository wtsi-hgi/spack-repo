# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMouse430a2Db(RPackage):
	"""Affymetrix Affymetrix Mouse430A_2 Array annotation data (chip mouse430a2)

	Affymetrix Affymetrix Mouse430A_2 Array annotation data (chip mouse430a2) assembled using data from public repositories
	"""
	
	bioc = "mouse430a2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mouse430a2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mouse430a2.db/mouse430a2.db_3.13.0.tar.gz"]

	version("3.13.0", md5="0f1d053517af5f973f3cc49289cca1e5")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.13:", type=("build", "run"))

