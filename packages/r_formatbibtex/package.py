# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormatbibtex(RPackage):
	"""Format BibTeX Entries and Files

	Format BibTeX entries and files in an opinionated way.
	"""
	
	homepage = "https://github.com/wenjie2wang/formatBibtex"
	cran = "formatBibtex" 

	version("0.1.0", md5="376e4763c3e418b0041e66aabb268fbc")

	depends_on("r@4:", type=("build", "run"))
