# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogler(RPackage):
	"""Google from the R Console

	This is a wrapper for the command line tool 'googler', which can be
    found at the following URL: <https://github.com/jarun/googler>.
	"""
	
	homepage = "https://github.com/mkearney/googler"
	cran = "googler" 

	version("0.0.1", md5="67f8344bce81b26ab52281e73e055e1e")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
