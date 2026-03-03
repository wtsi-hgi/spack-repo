# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtf(RPackage):
	"""Rich Text Format (RTF) Output

	A set of R functions to output Rich Text Format (RTF) files with high resolution tables and graphics that may be edited with a standard word processor such as Microsoft Word.
	"""
	
	homepage = "https://github.com/schaffman5/rtf"
	cran = "rtf" 

	version("0.4-14.1", md5="b3afa99fabe3b95a92937812db98acbc")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
