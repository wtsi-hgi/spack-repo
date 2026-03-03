# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRchoicedialogs(RPackage):
	"""'rChoiceDialogs' Collection

	Collection of portable choice dialog widgets.
	"""
	
	cran = "rChoiceDialogs" 

	version("1.0.6.1", md5="787ececb3a02f73d9e6acbadb45abe72")

	depends_on("r-rjava", type=("build", "run"))
