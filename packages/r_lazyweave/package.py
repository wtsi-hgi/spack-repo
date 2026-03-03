# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazyweave(RPackage):
	"""LaTeX Wrappers for R Users

	Provides the functionality to write LaTeX code from within R
    without having to learn LaTeX.  Functionality also exists to create HTML
    and Markdown code.  While the functionality still exists to write
    complete documents with lazyWeave, it is generally easier to do so with
    with markdown and knitr.  lazyWeave's main strength now is the ability
    to design custom and complex tables for reporting results.
	"""
	
	cran = "lazyWeave" 

	version("3.0.2", md5="e1a0c5821b29d4733eba04f076eb2634")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-labelvector", type=("build", "run"))
