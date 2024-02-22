# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathlit(RPackage):
	"""An SDK for the PathLit Engine

	This wrapper houses PathLit API endpoints for R. The usage of
    these endpoints require the use of an API key which can be obtained at
    <https://www.pathlit.io/docs/cli/>.
	"""
	
	homepage = "https://www.pathlit.io"
	cran = "pathlit" 

	version("0.1.0", md5="2eca3799c03df52b66481d7140dce64e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
