# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeyl(RPackage):
	"""The Weyl Algebra

	A suite of routines for Weyl algebras.  Notation follows
   Coutinho (1995, ISBN 0-521-55119-6, "A Primer of Algebraic
   D-Modules").  Uses 'disordR' discipline
   (Hankin 2022 <doi:10.48550/ARXIV.2210.03856>).  To cite
   the package in publications, use Hankin
   2022 <doi:10.48550/ARXIV.2212.09230>.
	"""
	
	homepage = "https://github.com/RobinHankin/weyl"
	cran = "weyl" 

	version("0.0-4", md5="5dc4deb59104fcdce89a30ee574f7eef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-disordr@0.0.8:", type=("build", "run"))
	depends_on("r-freealg@1.0.4:", type=("build", "run"))
	depends_on("r-spray@1.0.19:", type=("build", "run"))
