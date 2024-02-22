# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLamw(RPackage):
	"""Lambert-W Function

	Implements both real-valued branches of the Lambert-W function
    (Corless et al, 1996) <doi:10.1007/BF02124750> without the need for
    installing the entire GSL.
	"""
	
	homepage = "https://github.com/aadler/lamW"
	cran = "lamW" 

	version("2.2.3", md5="50f63b6975649dc1fce780e6c69c54e9")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
