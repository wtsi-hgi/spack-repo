# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadstata13(RPackage):
	"""Import 'Stata' Data Files

	Function to read and write the 'Stata' file format.
	"""
	
	homepage = "https://github.com/sjewo/readstata13"
	cran = "readstata13" 

	version("0.10.1", md5="be706d28f4575a4b5ac455ffc3a2a8a7", url="https://cran.r-project.org/src/contrib/readstata13_0.10.1.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
