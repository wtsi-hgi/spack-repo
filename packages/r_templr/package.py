# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTemplr(RPackage):
	"""MASCOTNUM Algorithms Template Tools

	Helper functions for MASCOTNUM algorithm template, for design of numerical experiments practice:
    algorithm template parser to support MASCOTNUM specification <https://www.gdr-mascotnum.fr/template.html>, 
    'ask & tell' decoupling injection (inspired by <https://search.r-project.org/CRAN/refmans/sensitivity/html/decoupling.html>) 
    to use "crimped" algorithms (like uniroot(), optim(), ...) from outside R,
    basic template examples: Brent algorithm for 1 dim root finding and L-BFGS-B from base optim().
	"""
	
	homepage = "https://github.com/MASCOTNUM/templr"
	cran = "templr" 

	version("0.2-0", md5="ce1aef7a593b58285f3c6fd411f3b1c8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
