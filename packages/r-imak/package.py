# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImak(RPackage):
	"""Item Maker

	This is an Automatic Item Generator for Psychological Assessment. Items created with the 'IMak' package should not be used in applied settings as part of the working protocol without ensuring first that the items meet the required psychometric quality standards (see Blum & Holling, 2018) <DOI:10.3389/fpsyg.2018.01286>.
	"""
	
	cran = "IMak" 

	version("2.1.0", md5="c10c8812a57f69d7e22a6c236fbbf342")

	depends_on("r-png", type=("build", "run"))
