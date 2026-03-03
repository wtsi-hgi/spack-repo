# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMassign(RPackage):
	"""Simple Matrix Construction

	Constructing matrices for quick prototyping can be a nuisance, 
    requiring the user to think about how to fill the matrix with values using 
    the matrix() function. The %<-% operator solves that issue by allowing the 
    user to construct matrices using code that shows the actual matrices.
	"""
	
	cran = "Massign" 

	version("1.1.0", md5="f809c953ad8ed610b5b220844cef96c9")

