# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdeps(RPackage):
	"""Identify External Packages Used in a Project

	Screens all '.R', '.Rmd', and '.qmd' files to extract the name of
    packages used in a project. This package detects packages called with 
    'library(foo)', 'require(foo)', and 'foo::bar()' and adds these 
    dependencies in the DESCRIPTION file in the sections Depends, Imports, and 
    Suggests.
	"""
	
	homepage = "https://github.com/frbcesab/rdeps"
	cran = "rdeps" 

	version("0.2", md5="99a85d4a3056fdbdb85c55b1b0f8832a")

	depends_on("r-cli", type=("build", "run"))
