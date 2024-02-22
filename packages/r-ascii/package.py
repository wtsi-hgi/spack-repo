# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAscii(RPackage):
	"""Export R Objects to Several Markup Languages

	Coerce R object to 'asciidoc', 'txt2tags',
    'restructuredText', 'org', 'textile' or 'pandoc' syntax.
    Package comes with a set of drivers for 'Sweave'.
	"""
	
	homepage = "https://github.com/mclements/ascii"
	cran = "ascii" 

	version("2.6", md5="a8f28de8e630050437d7508d8cc814fa")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
