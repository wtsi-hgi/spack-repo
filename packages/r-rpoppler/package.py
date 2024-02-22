# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpoppler(RPackage):
	"""PDF Tools Based on Poppler

	PDF tools based on the Poppler PDF rendering library.
  See <http://poppler.freedesktop.org/> for more information on Poppler.
	"""
	
	cran = "Rpoppler" 

	version("0.1-2", md5="1e86a48805836ee83372c0db7a46156d")

	depends_on("poppler+glib", type=("build", "link", "run"))
