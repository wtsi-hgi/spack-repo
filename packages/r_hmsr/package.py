# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmsr(RPackage):
	"""Multipopulation Evolutionary Strategy HMS

	
  The HMS (Hierarchic Memetic Strategy) is a composite global optimization
  strategy consisting of a multi-population evolutionary strategy and some
  auxiliary methods. The HMS makes use of a dynamically-evolving data structure
  that provides an organization among the component populations. It is a tree
  with a fixed maximal height and variable internal node degree. Each component
  population is governed by a particular evolutionary engine. This package
  provides a simple R implementation with examples of using different genetic
  algorithms as the population engines. References: J. Sawicki, M. Łoś,
  M. Smołka, J. Alvarez-Aramberri (2022) <doi:10.1007/s11047-020-09836-w>.
	"""
	
	homepage = "https://wojtacht.github.io/hms/"
	cran = "hmsr" 

	version("1.0.1", md5="d723669004292d3dfe82453dca8c0140")

	depends_on("r-ga", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
