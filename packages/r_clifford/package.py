# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClifford(RPackage):
	"""Arbitrary Dimensional Clifford Algebras

	A suite of routines for Clifford algebras, using the
   'Map' class of the Standard Template Library.  Canonical
   reference: Hestenes (1987, ISBN 90-277-1673-0, "Clifford algebra
   to geometric calculus").  Special cases including Lorentz transforms,
   quaternion multiplication, and Grassman algebra, are discussed.
   Conformal geometric algebra theory is implemented.  Uses 'disordR'
   discipline.
	"""
	
	homepage = "https://github.com/RobinHankin/clifford"
	cran = "clifford" 

	version("1.0-8", md5="bddff58a7c7a41da059223a6481574e4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-disordr@0.0.8:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-partitions@1.10.4:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
