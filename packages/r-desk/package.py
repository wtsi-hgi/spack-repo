# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesk(RPackage):
	"""Didactic Econometrics Starter Kit

	Written to help undergraduate as well as graduate students to get started
    with R for basic econometrics without the need to import specific functions
    and datasets from many different sources. Primarily, the package is meant to 
    accompany the German textbook Auer, L.v., Hoffmann, S., Kranz, T. (2023,
    ISBN: 978-3-662-68263-0) from which the exercises cover all the topics from the textbook
    Auer, L.v. (2023, ISBN: 978-3-658-42699-6).
	"""
	
	homepage = "https://github.com/OvGU-SH/desk"
	cran = "desk" 

	version("1.1.1", md5="61123182f68e27fcd54eb93d92bb32ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
