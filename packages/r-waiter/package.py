# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RWaiter(RPackage):
	"""Loading Screen for 'Shiny'

	Full screen and partial loading screens for 'Shiny' with spinners, progress bars, and notifications.
	"""
	
	homepage = "https://waiter.john-coene.com/"
	cran = "waiter" 

	version("0.2.5", md5="505258470d7de0f7be3ee3e23f495821")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
