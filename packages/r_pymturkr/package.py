# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPymturkr(RPackage):
	"""A Client for the 'MTurk' Requester API

	Provides access to the latest 'Amazon Mechanical Turk' ('MTurk') <https://www.mturk.com> Requester API (version '2017–01–17'), replacing the now deprecated 'MTurkR' package.
	"""
	
	cran = "pyMTurkR" 

	version("1.1.5", md5="8c10a707a141a2e1077635a939c8c684")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
