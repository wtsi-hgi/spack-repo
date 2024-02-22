# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIo(RPackage):
	"""A Unified Framework for Input-Output Operations in R

	One function to read files. One function to write files. One
    function to direct plots to screen or file. Automatic file format inference
    and directory structure creation.
	"""
	
	homepage = "https://bitbucket.org/djhshih/io"
	cran = "io" 

	version("0.3.2", md5="17e31e8971278d4b8a5f90b79312c70d")

	depends_on("r-filenamer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
