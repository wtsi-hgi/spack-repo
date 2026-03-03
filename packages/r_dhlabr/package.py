# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhlabr(RPackage):
	"""National Library of Norway Quantitative Text Data API Tools

	Tools for accessing data from National Library of Norway's dhlab (digital humanities laboratory).
    Provides wrappers for accessing our API services at <https://api.nb.no/dhlab/>.
    To learn more about dhlab, visit out site <https://www.nb.no/dh-lab/>.
	"""
	
	cran = "dhlabR" 

	version("1.0.2", md5="4fccd217f5be5e7bbcae3ca6821dbf83")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
