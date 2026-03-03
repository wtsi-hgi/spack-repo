# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrmtools(RPackage):
	"""Tools for Quantitative Risk Management

	Functions and data sets for reproducing selected results from
  the book "Quantitative Risk Management: Concepts, Techniques and Tools".
  Furthermore, new developments and auxiliary functions for Quantitative
  Risk Management practice.
	"""
	
	cran = "qrmtools" 

	version("0.0-17", md5="46d953e3db4bb23e3d96c2cd7b221931")
	version("0.0-16", md5="cc883a71e16ba4c494bef70d47e8ae1b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-quandl", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
