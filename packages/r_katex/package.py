# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKatex(RPackage):
	"""Rendering Math to HTML, 'MathML', or R-Documentation Format

	Convert latex math expressions to HTML and 'MathML' for use in 
    markdown documents or package manual pages. The rendering is done in 
    R using the V8 engine (i.e. server-side), which eliminates the need 
    for embedding the 'MathJax' library into your web pages. In addition
    a 'math-to-rd' wrapper is provided to automatically render beautiful
    math in R documentation files.
	"""
	
	homepage = "https://docs.ropensci.org/katex/"
	cran = "katex" 

	version("1.4.1", md5="02c798386ec307cbba60cf547c9351de")

	depends_on("r-v8", type=("build", "run"))
