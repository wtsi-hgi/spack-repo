# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenset(RPackage):
	"""Generates Data Sets for Class Demonstrations

	For educational purposes to demonstrate the importance of multiple regression. The genset function generates a data set from an initial data set to have the same summary statistics (mean, median, and standard deviation) but opposing regression results.
	"""
	
	cran = "genset" 

	version("0.1.0", md5="980d27648bbe7367452a3509f788bb68")

