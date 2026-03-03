# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImportinegi(RPackage):
	"""Download and Manage Open Data from INEGI

	Download and manage data sets of statistical projects and geographic data created by Instituto Nacional de Estadistica y Geografia (INEGI). See <https://www.inegi.org.mx/>.
	"""
	
	cran = "importinegi" 

	version("1.2.1", md5="37ce46ad520c2c4e03a42a4803ee5b05")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
