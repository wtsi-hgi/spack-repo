# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgug4131aDb(RPackage):
	"""Agilent "Rat Genome, Whole" annotation data (chip rgug4131a)

	Agilent "Rat Genome, Whole" annotation data (chip rgug4131a) assembled using data from public repositories
	"""
	
	bioc = "rgug4131a.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rgug4131a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rgug4131a.db/rgug4131a.db_3.2.3.tar.gz"]

	version("3.2.3", md5="1168d4906fb8ce60cbc0fa6cfa3b8ec6")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.3:", type=("build", "run"))

