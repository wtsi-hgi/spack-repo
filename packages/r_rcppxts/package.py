# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppxts(RPackage):
	"""Interface the 'xts' API via 'Rcpp'

	Access to some of the C level functions of the 'xts' package.  
 In its current state, the package is mostly a proof-of-concept to support
 adding useful functions, and does not yet add any of its own.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppxts"
	cran = "RcppXts" 

	version("0.0.6", md5="9553845743109657c5e6ea9df4a65a97")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
