# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntmap(RPackage):
	"""Ordered Containers with Integer Keys

	Provides a key-value store data structure. The keys are
    integers and the values can be any R object. This is like a list but
    indexed by a set of integers, not necessarily contiguous and possibly
    negative. The implementation uses a 'R6' class. These containers are 
    not faster than lists but their usage can be more convenient for 
    certain situations.
	"""
	
	homepage = "https://github.com/stla/intmap"
	cran = "intmap" 

	version("1.0.0", md5="77e5f53e513ac1e4c6b65906f427d734")

	depends_on("r-maybe", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
