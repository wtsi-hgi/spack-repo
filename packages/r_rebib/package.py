# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebib(RPackage):
	"""Convert and Aggregate Bibliographies

	Authors working with 'LaTeX' articles use the built-in bibliography
    options and 'BibTeX' files. While this might work with 'LaTeX', it does not
    function well with Web articles. As a way out, 'rebib' offers tools to
    convert and combine bibliographies from both sources. 
	"""
	
	homepage = "https://github.com/Abhi-1U/rebib"
	cran = "rebib" 

	version("0.3.2", md5="0c1d792d3c761c0c57b9f85085ea0ea5")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
