# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinydatetimepickers(RPackage):
	"""Some Datetime Pickers for 'Shiny'

	Provides three types of datetime pickers for usage in a
    'Shiny' UI. A datetime picker is an input field for selecting both a
    date and a time.
	"""
	
	homepage = "https://github.com/stla/shinyDatetimePickers"
	cran = "shinyDatetimePickers" 

	version("1.1.0", md5="14aa7470dfadc516cde4ed974fce1039")

	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-reactr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
