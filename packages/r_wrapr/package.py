# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrapr(RPackage):
	"""Wrap R Tools for Debugging and Parametric Programming

	Tools for writing and debugging R code. Provides: 
    '%.>%' dot-pipe (an 'S3' configurable pipe), unpack/to (R style multiple assignment/return),
    'build_frame()'/'draw_frame()' ('data.frame' example tools),
    'qc()' (quoting concatenate), 
    ':=' (named map builder), 'let()' (converts non-standard evaluation interfaces to parametric standard
    evaluation interfaces, inspired by 'gtools::strmacro()' and 'base::bquote()'), and more.
	"""
	
	homepage = "https://github.com/WinVector/wrapr"
	cran = "wrapr" 

	version("2.1.0", md5="8f50c87b40f26b867b3f96f19720eabe")

	depends_on("r@3.3:", type=("build", "run"))
