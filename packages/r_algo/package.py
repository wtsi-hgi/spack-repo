# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlgo(RPackage):
	"""Implement an Address Search Auto Completion Menu on 'Shiny' Text
Inputs Using the 'Algolia Places' 'Javascript' Library

	Allows the user to implement an address search auto completion menu on 'shiny' text inputs.
    This is done using the 'Algolia Places' 'JavaScript' library. See <https://community.algolia.com/places/>.
	"""
	
	homepage = "https://github.com/feddelegrand7/algo"
	cran = "algo" 

	version("0.1.0", md5="eaf49fdeced2a67e91a5642fff869d4f")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
