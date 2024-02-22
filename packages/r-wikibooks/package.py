# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWikibooks(RPackage):
	"""Functions and Datasets of the German WikiBook "GNU R"

	The german Wikibook "GNU R" introduces R to new users. This package is a collection of functions and datas used in the german WikiBook "GNU R".
	"""
	
	homepage = "https://de.wikibooks.org/wiki/GNU_R"
	cran = "wikibooks" 

	version("0.2.1", md5="d4486e2b57da5410cde93e172e131513")

	depends_on("r@2.1:", type=("build", "run"))
