# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgu34bDb(RPackage):
	"""Affymetrix Affymetrix RG_U34B Array annotation data (chip rgu34b)

	Affymetrix Affymetrix RG_U34B Array annotation data (chip rgu34b) assembled using data from public repositories
	"""
	
	bioc = "rgu34b.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgu34b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgu34b.db/rgu34b.db_3.13.0.tar.gz"]

	version("3.13.0", md5="5aeb80d5190bf2dcffa6b9264d3db33f")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

