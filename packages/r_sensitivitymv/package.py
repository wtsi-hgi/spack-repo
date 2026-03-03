# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivitymv(RPackage):
	"""Sensitivity Analysis in Observational Studies

	The package performs a sensitivity analysis in an observational study using an M-statistic, for instance, the mean.  The main function in the package is senmv(), but amplify() and truncatedP() are also useful.  The method is developed in Rosenbaum Biometrics, 2007, 63, 456-464, <doi:10.1111/j.1541-0420.2006.00717.x>.
	"""
	
	cran = "sensitivitymv" 

	version("1.4.3", md5="5fb32692468cd508fd6cf12ec8df18b7")

