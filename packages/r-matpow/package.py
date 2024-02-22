# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatpow(RPackage):
	"""Matrix Powers

	A general framework for computing powers of matrices.  A
   key feature is the capability for users to write callback functions,
   called after each iteration, thus enabling customization for specific
   applications.  Diverse types of matrix classes/matrix multiplication
   are accommodated.  If the multiplication type computes in parallel,
   then the package computation is also parallel.
	"""
	
	cran = "matpow" 

	version("0.1.2", md5="45cacdc0b68965b7221269c702219fc2")

