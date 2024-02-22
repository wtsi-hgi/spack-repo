# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScor(RPackage):
	"""Spherically Constrained Optimization Routine

	A non convex optimization package that optimizes any function under the criterion, combination of variables are on the surface of a unit sphere, as described in the paper : Das et al. (2019) <arXiv:1909.04024> .
	"""
	
	homepage = "https://github.com/synx21/SCOR"
	cran = "SCOR" 

	version("1.1.2", md5="bd561c97cf754b3986bae68360790a8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
