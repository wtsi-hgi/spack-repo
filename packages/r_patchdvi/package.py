# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatchdvi(RPackage):
	"""Package to Patch '.dvi' or '.synctex' Files

	Functions to patch specials in '.dvi' files,
        or entries in '.synctex' files.  Works with concordance=TRUE 
        in Sweave, knitr or R Markdown to link sources to previews.
	"""
	
	homepage = "https://github.com/dmurdoch/patchDVI"
	cran = "patchDVI" 

	version("1.11.0", md5="95d3c2f4cc511735dbba3a6dd05b3f2f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rmdconcord", type=("build", "run"))
