# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttptest(RPackage):
	"""A Test Environment for HTTP Requests

	Testing and documenting code that communicates with remote servers
    can be painful. Dealing with authentication, server state,
    and other complications can make testing seem too costly to
    bother with. But it doesn't need to be that hard. This package enables one
    to test all of the logic on the R sides of the API in your package without
    requiring access to the remote service. Importantly, it provides three
    contexts that mock the network connection in different ways, as well as
    testing functions to assert that HTTP requests were---or were
    not---made. It also allows one to safely record real API responses to use as
    test fixtures. The ability to save responses and load them offline also
    enables one to write vignettes and other dynamic documents that can be
    distributed without access to a live server.
	"""
	
	homepage = "https://enpiar.com/r/httptest/"
	cran = "httptest" 

	version("4.2.2", md5="e86f108b59cb5ef0650dc7c73f09ed87")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
