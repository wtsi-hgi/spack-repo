# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebusUnicode(RPackage):
	"""Unicode Extensions for the 'rebus' Package

	Build regular expressions piece by piece using human readable code.
    This package contains Unicode functionality, and is primarily intended to be
    used by package developers.
	"""
	
	cran = "rebus.unicode" 

	version("0.0-2", md5="e1ad36113be3b809e1a03e2fa235c22c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rebus-base@0.0.2:", type=("build", "run"))
