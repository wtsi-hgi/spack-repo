# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmatio(RPackage):
	"""Read and Write 'Matlab' Files

	Read and write 'Matlab' MAT files from R. The 'rmatio'
    package supports reading MAT version 4, MAT version 5 and MAT
    compressed version 5. The 'rmatio' package can write version 5 MAT
    files and version 5 files with variable compression.
	"""
	
	homepage = "https://github.com/stewid/rmatio"
	cran = "rmatio" 

	version("0.19.0", md5="fd2f537028586160c1c52b3218143a37")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
