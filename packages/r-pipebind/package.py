# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPipebind(RPackage):
	"""Flexible Binding for Complex Function Evaluation with the Base R
|> Pipe

	Provides a simple function to bind a piped object to a placeholder
    symbol to enable complex function evaluation with the base R |> pipe.
	"""
	
	homepage = "https://github.com/bwiernik/pipebind/"
	cran = "pipebind" 

	version("0.1.2", md5="a9dd266018593a41d14a8d62bb0585bc")

