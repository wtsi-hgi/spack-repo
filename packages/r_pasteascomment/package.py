# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPasteascomment(RPackage):
	"""'RStudio' Addin to Paste the Clipboard as a Comment Block or a
'roxygen' Block

	Provides a 'RStudio' addin allowing to paste the content of the clipboard as a comment block or as 'roxygen' lines. This is very useful to insert an example in the 'roxygen' block.
	"""
	
	homepage = "https://github.com/stla/pasteAsComment"
	cran = "pasteAsComment" 

	version("0.2.1", md5="e9a0c02154707210daaa796ded64396e")

	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
