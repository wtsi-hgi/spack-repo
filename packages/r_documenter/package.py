# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocumenter(RPackage):
	"""Documents Files

	It is sometimes necessary to create documentation for all files in a directory. Doing so by hand can be very tedious. This task is made fast and reproducible using the functionality of 'documenter'. It aggregates all text files in a directory and its subdirectories into a single word document in a semi-automated fashion.
	"""
	
	cran = "documenter" 

	version("0.1.3", md5="1f7f887410f81a7c6a6fb42ade4c9bf2")

	depends_on("r-officer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
