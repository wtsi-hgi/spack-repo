# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadysignal(RPackage):
	"""'Ready Signal' API Wrapper

	A simple way to interact with the 'Ready Signal' API without
    leaving your 'R' environment. Discover features, manage signals, and retrieve data easily.
    View the full API documentation at <https://readysignal.com/ready-signal-api-documentation/>.
	"""
	
	cran = "readysignal" 

	version("0.0.9", md5="f1f4bbee9753ca9812e4c2a550fe6b41")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
