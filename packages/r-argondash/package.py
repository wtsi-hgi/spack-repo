# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgondash(RPackage):
	"""Argon Shiny Dashboard Template

	Create awesome 'Bootstrap 4' dashboards powered by 'Argon'.
   See more here <https://rinterface.github.io/argonDash/>.
	"""
	
	homepage = "https://github.com/RinteRface/argonDash"
	cran = "argonDash" 

	version("0.2.0", md5="e8746c7a5045621139a5f72d638428f3")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-argonr", type=("build", "run"))
