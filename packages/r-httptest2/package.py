# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHttptest2(RPackage):
	"""Test Helpers for 'httr2'

	Testing and documenting code that communicates with remote servers
    can be painful. This package helps with writing tests for packages that
    use 'httr2'. It enables testing all of the logic
    on the R sides of the API without requiring access to the
    remote service, and it also allows recording real API responses to use as
    test fixtures. The ability to save responses and load them offline also
    enables writing vignettes and other dynamic documents that can be
    distributed without access to a live server.
	"""
	
	homepage = "https://enpiar.com/httptest2/"
	cran = "httptest2" 

	version("1.0.0", md5="b468ca0dd8c209ab7167c359bb17370e", url="https://cran.r-project.org/src/contrib/httptest2_1.0.0.tar.gz")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
