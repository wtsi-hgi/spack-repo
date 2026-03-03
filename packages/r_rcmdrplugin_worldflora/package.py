# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginWorldflora(RPackage):
	"""R Commander Plug-in for the 'WorldFlora' Package

	An R Commander plug-in for the 'WorldFlora' package. It was mainly developed to show work flows and scripts for first-time users.
	"""
	
	cran = "RcmdrPlugin.WorldFlora" 

	version("1.3", md5="4c181f6d7ed90c94d0422655da815049")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-worldflora@1.13.2:", type=("build", "run"))
	depends_on("r-rcmdr@2.4.0:", type=("build", "run"))
