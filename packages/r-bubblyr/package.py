# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBubblyr(RPackage):
	"""Beautiful Bubbles for 'shiny' and 'rmarkdown' Backgrounds

	Creates bubbles within 'shiny' and 'rmarkdown' backgrounds using the 'bubbly-bg' 'JavaScript' library.
	"""
	
	homepage = "https://github.com/feddelegrand7/bubblyr"
	cran = "bubblyr" 

	version("0.1.2", md5="cff32e92a59d83d142687fa28b75ff67")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
