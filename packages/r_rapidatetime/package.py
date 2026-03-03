# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidatetime(RPackage):
	"""R API for 'Date' and 'Datetime'

	Access to the C-level R date and 'datetime' code is provided for
 C-level API use by other packages via registration of native functions.
 Client packages simply include a single header 'RApiDatetime.h' provided
 by this package, and also 'import' it.  The R Core group is the original
 author of the code made available with slight modifications by this package. 
	"""
	
	homepage = "https://github.com/eddelbuettel/rapidatetime"
	cran = "RApiDatetime" 

	version("0.0.9", md5="97291cb2261cfb34855e7e278ea8f7e2")

