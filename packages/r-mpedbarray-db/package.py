# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpedbarrayDb(RPackage):
	"""FHCRC Nelson Lab mpedbarray Annotation Data (mpedbarray)

	FHCRC Nelson Lab mpedbarray Annotation Data (mpedbarray) assembled using data from public repositories
	"""
	
	bioc = "mpedbarray.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mpedbarray.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mpedbarray.db/mpedbarray.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="91ec9e23dde36eb5de74e14654d46e2f27422db02a656c2d5729acbf2364fc12")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))

