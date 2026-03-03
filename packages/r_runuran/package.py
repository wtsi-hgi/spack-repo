# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunuran(RPackage):
	"""R Interface to the 'UNU.RAN' Random Variate Generators

	Interface to the 'UNU.RAN' library for Universal Non-Uniform RANdom variate generators. 
	     Thus it allows to build non-uniform random number generators from quite arbitrary
	     distributions. In particular, it provides an algorithm for fast numerical inversion
	     for distribution with given density function.
	     In addition, the package contains densities, distribution functions and quantiles
	     from a couple of distributions. 
	"""
	
	homepage = "https://statmath.wu.ac.at/unuran/"
	cran = "Runuran" 

	version("0.38", md5="93bba2ab1e5ccb855ee8a5bb6c162614")

	depends_on("r@3:", type=("build", "run"))
