# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImportexport(RPackage):
	"""Import and Export Data

	Import and export data from the most common statistical formats by using 
	     R functions that guarantee the least loss of the data information, giving special
	     attention to the date variables and the labelled ones.
	"""
	
	cran = "ImportExport" 

	version("1.3", md5="532f7cfb49f725f48d51daae18a1f377")

	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
