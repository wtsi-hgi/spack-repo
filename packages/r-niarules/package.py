# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNiarules(RPackage):
	"""Numerical Association Rule Mining using Population-Based
Nature-Inspired Algorithms

	Framework is devoted to mining numerical association rules through the
  utilization of nature-inspired algorithms for optimization. Drawing inspiration
  from the 'NiaARM' 'Python' and the 'NiaARM' 'Julia' packages, this repository
  introduces the capability to perform numerical association rule mining in
  the R programming language.
  Fister Jr., Iglesias, Galvez, Del Ser, Osaba and Fister (2018) <doi:10.1007/978-3-030-03493-1_9>.
	"""
	
	homepage = "https://github.com/firefly-cpp/niarules"
	cran = "niarules" 

	version("0.1.0", md5="1f0e337dd57c59d19710f536196f551a")

	depends_on("r@4:", type=("build", "run"))
