# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItertools2(RPackage):
	"""itertools2: Functions creating iterators for efficient looping

	A port of Python's excellent itertools module to R for efficient
    looping.
	"""
	
	homepage = "https://github.com/ramhiser/itertools2"
	cran = "itertools2" 

	version("0.1.1", md5="11471dc0d0e8b1feddc4264a2fb7d13c", url="https://cran.r-project.org/src/contrib/itertools2_0.1.1.tar.gz")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-iterators@1.0.7:", type=("build", "run"))
