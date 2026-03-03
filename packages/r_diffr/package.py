# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffr(RPackage):
	"""Display Differences Between Two Files using Codediff Library

	An R interface to the 'codediff' JavaScript library (a copy of which is included in the package,
  see <https://github.com/danvk/codediff.js> for information).
  Allows for visualization of the difference between 2 files, usually text files or R scripts, in a browser.
	"""
	
	cran = "diffr" 

	version("0.1", md5="63875a2d2113b175628bc2270e8193aa")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
