# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJordan(RPackage):
	"""A Suite of Routines for Working with Jordan Algebras

	A Jordan algebra is an algebraic object originally
   designed to study observables in quantum mechanics.  Jordan
   algebras are commutative but non-associative; they satisfy the
   Jordan identity.  The package follows the ideas and notation of
   K. McCrimmon (2004, ISBN:0-387-95447-3) "A Taste of Jordan
   Algebras".  To cite in publications please use Hankin (2023)
   <arXiv:2303.06062v1>.
	"""
	
	homepage = "https://github.com/RobinHankin/jordan"
	cran = "jordan" 

	version("1.0-5", md5="56aac0cf42c4e8ff3ff7d10ed46a9e3e")
	version("1.0-1", md5="d077f32b6d9bfe43b55d4916c393aa2b")

	depends_on("r-onion@1.4.0:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-emulator", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
