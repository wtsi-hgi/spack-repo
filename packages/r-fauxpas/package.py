# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFauxpas(RPackage):
	"""HTTP Error Helpers

	HTTP error helpers. Methods included for general purpose HTTP 
    error handling, as well as individual methods for every HTTP status
    code, both via status code numbers as well as their descriptive names.
    Supports ability to adjust behavior to stop, message or warning.
    Includes ability to use custom whisker template to have any configuration
    of status code, short description, and verbose message. Currently 
    supports integration with 'crul', 'curl', and 'httr'.
	"""
	
	homepage = "https://sckott.github.io/fauxpas/"
	cran = "fauxpas" 

	version("0.5.2", md5="6ee52b2a7c648240502bbb8b57a2222e")

	depends_on("r-r6@2.1.2:", type=("build", "run"))
	depends_on("r-httpcode@0.3:", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
