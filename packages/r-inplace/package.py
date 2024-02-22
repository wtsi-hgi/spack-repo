# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInplace(RPackage):
	"""In-place Operators for R

	It provides in-place operators for R 
    that are equivalent to '+=', '-=', '*=', '/=' in C++. 
    Those can be applied on integer|double vectors|matrices.
    You have also access to sweep operations (in-place).
	"""
	
	homepage = "https://github.com/privefl/inplace"
	cran = "inplace" 

	version("0.1.2", md5="528cc3969fee3e27feb072d8aa98190f")

	depends_on("r-rcpp", type=("build", "run"))
