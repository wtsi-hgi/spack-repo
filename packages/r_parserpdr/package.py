# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParserpdr(RPackage):
	"""Parse and Manipulate Research Patient Data Registry ('RPDR')
Text Queries

	Functions to load Research Patient Data Registry ('RPDR') text queries from Partners Healthcare institutions into R.
             The package also provides helper functions to manipulate data and execute common procedures
             such as finding the closest radiological exams considering a given timepoint, or creating a DICOM header database
             from the downloaded images. All functionalities are parallelized for fast and efficient analyses.
	"""
	
	homepage = "https://github.com/martonkolossvary/parseRPDR"
	cran = "parseRPDR" 

	version("1.1.1", md5="bc683bafe539143ab3cabd3377718622")
	version("1.1.0", md5="5051549700dc7df1a7c7c927a889d5e8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.14.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-parallelly@1.36:", type=("build", "run"))
	depends_on("r-foreach@1.5.1:", type=("build", "run"))
	depends_on("r-future@1.33.1:", type=("build", "run"))
	depends_on("r-dofuture@1.0.1:", type=("build", "run"))
	depends_on("r-progressr@0.14:", type=("build", "run"))
