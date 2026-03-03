# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvent(RPackage):
	"""Event History Procedures and Models

	Functions for setting up and analyzing event history data.
	"""
	
	homepage = "http://www.commanster.eu/rcode.html"
	cran = "event" 

	version("1.1.1", md5="196e59172636b32fcb10479c8f52f109")

	depends_on("r@1.4:", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
