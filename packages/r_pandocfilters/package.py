# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPandocfilters(RPackage):
	"""Pandoc Filters for R

	The document converter 'pandoc' <https://pandoc.org/> is widely used
    in the R community. One feature of 'pandoc' is that it can produce and consume
    JSON-formatted abstract syntax trees (AST). This allows to transform a given
    source document into JSON-formatted AST, alter it by so called filters and pass
    the altered JSON-formatted AST back to 'pandoc'. This package provides functions
    which allow to write such filters in native R code. 
    Although this package is inspired by the Python package 'pandocfilters' 
    <https://github.com/jgm/pandocfilters/>, it provides additional convenience functions which make it simple to use the 'pandocfilters' package as a 
    report generator. Since 'pandocfilters' inherits most of it's functionality
    from 'pandoc' it can create documents in many formats 
    (for more information see <https://pandoc.org/>) but is also bound to the same
    limitations as 'pandoc'.
	"""
	
	homepage = "https://pandoc.org/"
	cran = "pandocfilters" 

	version("0.1-6", md5="3c7cbd98a0ebedc78c5ebde53f7cd58b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("pandoc@1.12:", type=("build", "link", "run"))
