# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwgcodDb(RPackage):
	"""Codelink Rat Whole Genome Bioarray (~34 000 rat gene targets) annotation data (chip rwgcod)

	Codelink Rat Whole Genome Bioarray (~34 000 rat gene targets) annotation data (chip rwgcod) assembled using data from public repositories
	"""
	
	bioc = "rwgcod.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rwgcod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rwgcod.db/rwgcod.db_3.4.0.tar.gz"]

	version("3.4.0", md5="c8d2fa81b6f03c4ee629a0883431e5fd")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.2.1:", type=("build", "run"))

	# annotation