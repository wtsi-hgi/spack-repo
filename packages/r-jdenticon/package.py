# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJdenticon(RPackage):
	"""A Wrapper for the Node.js 'Jdenticon' Library

	A Wrapper for the Node.js 'Jdenticon' <https://jdenticon.com/> Library. Uses 'esbuild' <https://esbuild.github.io/> to reduce user dependencies.  
	"""
	
	cran = "jdenticon" 

	version("0.1.1", md5="5272f11d436f685d6e1eab7959316262")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-yesno", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
