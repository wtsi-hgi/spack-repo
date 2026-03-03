# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhandsontable(RPackage):
	"""Interface to the 'Handsontable.js' Library

	An R interface to the 'Handsontable' JavaScript library, which is a
    minimalist Excel-like data grid editor.  See <https://handsontable.com/> for details.
	"""
	
	homepage = "http://jrowen.github.io/rhandsontable/"
	cran = "rhandsontable" 

	version("0.3.8", md5="349303d13b2915de63f6d6e2fa9eb51e")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmlwidgets@0.3.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
