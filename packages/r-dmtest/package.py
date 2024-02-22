# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmtest(RPackage):
	"""Differential Methylation Tests (DMtest)

	Several tests for differential methylation in methylation array data, including one-sided differential mean and variance test. Methods used in the package refer to Dai, J, Wang, X, Chen, H and others (2021) "Incorporating increased variability in discovering cancer methylation markers", Biostatistics, submitted.
	"""
	
	cran = "DMtest" 

	version("1.0.0", md5="1294574ae7346fbf71f549c519621cc1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
