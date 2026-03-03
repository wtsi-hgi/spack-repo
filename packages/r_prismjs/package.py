# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrismjs(RPackage):
	"""Server-Side Syntax Highlighting

	Prism <https://prismjs.com/> is a lightweight, extensible syntax 
    highlighter, built with modern web standards in mind. This package provides 
    server-side rendering in R using 'V8' such that no JavaScript library is
    required in the resulting HTML documents. Over 400 languages are supported.
	"""
	
	homepage = "https://github.com/ropensci/prismjs"
	cran = "prismjs" 

	version("1.1.0", md5="f36e51f9c6afc0e5580b73eeb713352b")

	depends_on("r-v8", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
