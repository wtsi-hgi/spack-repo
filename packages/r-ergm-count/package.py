# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmCount(RPackage):
	"""Fit, Simulate and Diagnose Exponential-Family Models for
Networks with Count Edges

	A set of extensions for the 'ergm' package to fit weighted networks whose edge weights are counts. See Krivitsky (2012) <doi:10.1214/12-EJS696> and Krivitsky, Hunter, Morris, and Klumb (2021) <arXiv:2106.04997>.
	"""
	
	homepage = "https://statnet.org"
	cran = "ergm.count" 

	version("4.1.1", md5="a4b511804c1fea5cdac72c1abeedf302")

	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-network@1.15:", type=("build", "run"))
	depends_on("r-statnet-common@4.2:", type=("build", "run"))
