# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStokes(RPackage):
	"""The Exterior Calculus

	Provides functionality for working with tensors, alternating
           forms, wedge products, Stokes's theorem, and related concepts
	   from the exterior calculus.   Uses 'disordR' discipline
	   (Hankin, 2022, <doi:10.48550/ARXIV.2210.03856>).  The
	   canonical reference would be M. Spivak
	   (1965, ISBN:0-8053-9021-9) "Calculus on Manifolds".  To cite
	   the package in publications please use Hankin (2022)
           <doi:10.48550/ARXIV.2210.17008>.
	"""
	
	homepage = "https://github.com/RobinHankin/stokes"
	cran = "stokes" 

	version("1.2-0", md5="b54c7be00e69afb82be806a3217b24cb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-permutations@1.1.2:", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-disordr@0.9.7:", type=("build", "run"))
	depends_on("r-spray@1.0.24:", type=("build", "run"))
