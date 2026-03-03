# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinystoreplus(RPackage):
	"""Secure in-Browser Storage for 'Shiny' Inputs, Outputs and
Variables

	Store persistent and synchronized data from 'Shiny' inputs within the browser in a secure format. Refresh 'Shiny' applications and preserve user-inputs over multiple sessions. A database-like storage format is implemented using 'Dexie.js' <https://dexie.org>, a minimal wrapper for 'IndexedDB'. Transfer browser link parameters to 'Shiny' input or output values.
	"""
	
	homepage = "https://shinystoreplus.obi.obianom.com"
	cran = "shinyStorePlus" 

	version("1.1", md5="304829fba36c4ee5bb47b627c5a18d09")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
