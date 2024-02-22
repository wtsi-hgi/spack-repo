# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdm(RPackage):
	"""Death Registration Coverage Estimation

	A set of three two-census methods to the estimate the degree of death registration coverage for a population. Implemented methods include the Generalized Growth Balance method (GGB), the Synthetic Extinct Generation method (SEG), and a hybrid of the two, GGB-SEG. Each method offers automatic estimation, but users may also specify exact parameters or use a graphical interface to guess parameters in the traditional way if desired.
	"""
	
	cran = "DDM" 

	version("1.0-0", md5="d081e6fe46290af15d9eac5907a66107")

	depends_on("r@2.15:", type=("build", "run"))
