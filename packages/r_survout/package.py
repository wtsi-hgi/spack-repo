# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvout(RPackage):
	"""Excel Conversion of R Surival Analysis Output

	Simple and quick method of exporting the most often used
    survival analysis results to an Excel sheet.
	"""
	
	cran = "survout" 

	version("0.1.0", md5="8c53c9ce73f63b3f3d5b18bf9bd60e3b")

	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
