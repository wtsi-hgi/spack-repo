# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPermutations(RPackage):
	"""The Symmetric Group: Permutations of a Finite Set

	Manipulates invertible functions from a finite set to
             itself.  Can transform from word form to cycle form and
             back.  To cite the package in publications please use
             Hankin (2020) "Introducing the permutations R package",
             SoftwareX, volume 11 <doi:10.1016/j.softx.2020.100453>.
	"""
	
	homepage = "https://github.com/RobinHankin/permutations"
	cran = "permutations" 

	version("1.1-2", md5="32346afb52a1826c45dc255fe2d4f750")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-partitions@1.9.17:", type=("build", "run"))
	depends_on("r-freealg@1.0.4:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
