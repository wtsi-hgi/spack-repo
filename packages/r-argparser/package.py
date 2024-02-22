# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgparser(RPackage):
	"""Command-Line Argument Parser

	Cross-platform command-line argument parser written purely in R
    with no external dependencies. It is useful with the Rscript
    front-end and facilitates turning an R script into an executable script.
	"""
	
	homepage = "https://bitbucket.org/djhshih/argparser"
	cran = "argparser" 

	version("0.7.1", md5="0048935b4101aef737e31ba02b9bdddb")

