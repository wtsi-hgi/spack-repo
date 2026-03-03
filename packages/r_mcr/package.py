# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcr(RPackage):
	"""Method Comparison Regression

	Regression methods to quantify the relation between two measurement
    methods are provided by this package. In particular it addresses regression
    problems with errors in both variables and without repeated measurements. It
    implements the CLSI recommendations (see J. A. Budd et al. 
    (2018, <https://clsi.org/standards/products/method-evaluation/documents/ep09/>) 
    for analytical method comparison and bias estimation using patient samples.
    Furthermore, algorithms for Theil-Sen and equivariant Passing-Bablok estimators 
    are implemented, see F. Dufey (2020, <doi:10.1515/ijb-2019-0157>) and 
    J. Raymaekers and F. Dufey (2022, <arXiv:2202:08060>).
    A comprehensive overview over the implemented methods and references can be found 
    in the manual pages "mcr-package" and "mcreg".
	"""
	
	cran = "mcr" 

	version("1.3.3", md5="b4121bc3370b08438a8ecde1d9231a1d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-robslopes", type=("build", "run"))
