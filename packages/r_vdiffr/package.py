# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdiffr(RPackage):
	"""Visual Regression Testing and Graphical Diffing

	An extension to the 'testthat' package that makes it easy
    to add graphical unit tests. It provides a Shiny application to
    manage the test cases.
	"""
	
	homepage = "https://vdiffr.r-lib.org/"
	cran = "vdiffr" 

	version("1.0.7", md5="392bc1fd9d13c621c5ad496e0548a828")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-diffobj", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-testthat@3.0.3:", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("libpng", type=("build", "link", "run"))
