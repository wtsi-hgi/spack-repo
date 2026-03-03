# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrimr(RPackage):
	"""An Implementation of Common Response Time Trimming Methods

	Provides various commonly-used response time trimming
    methods, including the recursive / moving-criterion methods reported by
    Van Selst and Jolicoeur (1994). By passing trimming functions raw data files,
    the package will return trimmed data ready for inferential testing.
	"""
	
	homepage = "https://github.com/JimGrange/trimr"
	cran = "trimr" 

	version("1.1.1", md5="05fdccc6d59a4faf4289bf7c8ad88ddb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
