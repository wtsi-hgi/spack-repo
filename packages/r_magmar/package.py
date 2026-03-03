# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagmar(RPackage):
	"""R-Client for Interacting with the 'UCSF Data Library'

	A client for interacting with 'magma', the data warehouse of the
    'UCSF Data Library'. 'magmaR' includes functions for querying and
    downloading data from 'magma', in order to enable working with such data in
    R, as well as for uploading local data to 'magma'.
	"""
	
	cran = "magmaR" 

	version("1.0.3", md5="0bc5106f26d73514904c0ce69f38129c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
