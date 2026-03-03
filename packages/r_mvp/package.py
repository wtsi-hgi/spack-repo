# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvp(RPackage):
	"""Fast Symbolic Multivariate Polynomials

	Fast manipulation of symbolic multivariate polynomials
  using the 'Map' class of the Standard Template Library.  The package
  uses print and coercion methods from the 'mpoly' package (Kahle
  2013, "Multivariate polynomials in R", The R Journal, 5(1):162), but
  offers speed improvements.  It is comparable in speed to the 'spray'
  package for sparse arrays, but retains the symbolic benefits of
  'mpoly'.  To cite the package in publications, use Hankin 2022
  <doi:10.48550/ARXIV.2210.15991>.  Uses 'disordR' discipline.
	"""
	
	homepage = "https://github.com/RobinHankin/mvp"
	cran = "mvp" 

	version("1.0-14", md5="c1c1fd777be400a1e8c90bde24fefb06")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mpoly@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-disordr@0.9:", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
