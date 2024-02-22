# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgwtools(RPackage):
	"""Miscellaneous Tools

	Functions for performing quick observations or evaluations of data, including a variety of ways to list objects by size, class, etc.  The functions 'seqle' and 'reverse.seqle' mimic the base 'rle' but can search for linear sequences. The function 'splatnd' allows the user to generate zero-argument commands without the need for 'makeActiveBinding' .  Functions provided to convert from any base to any other base, and to find the n-th greatest max or n-th least min.  In addition, functions which mimic Unix shell commands, including 'head', 'tail' ,'pushd' ,and 'popd'. Various other goodies included as well. 
	"""
	
	cran = "cgwtools" 

	version("4.1", md5="5340c423af908f8ceefd2bd5c813c8b4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
