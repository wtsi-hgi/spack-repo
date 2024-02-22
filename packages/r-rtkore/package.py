# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtkore(RPackage):
	"""'STK++' Core Library Integration to 'R' using 'Rcpp'

	'STK++' <http://www.stkpp.org> is a collection of C++ classes
    for statistics, clustering, linear algebra, arrays (with an 'Eigen'-like API),
    regression, dimension reduction, etc. The integration of the library to 'R' is
    using 'Rcpp'. The 'rtkore' package includes the header files from the 'STK++'
    core library. All files contain only template classes and/or inline functions.
    'STK++' is licensed under the GNU LGPL version 2 or later. 'rtkore' (the 'stkpp'
    integration into 'R') is licensed under the GNU GPL version 2 or later. See file
    LICENSE.note for details.
	"""
	
	homepage = "http://www.stkpp.org"
	cran = "rtkore" 

	version("1.6.10", md5="7d3647bce2b7b9b7236d195c4909f28c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
