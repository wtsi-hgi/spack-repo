# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtinference(RPackage):
	"""Inference for Optimal Transport

	Sample from the limiting distributions of empirical Wasserstein
    distances under the null hypothesis and under the alternative. Perform a 
    two-sample test on multivariate data using these limiting distributions and 
    binning.
	"""
	
	cran = "otinference" 

	version("0.1.0", md5="a88c31a3defd8c5bf12969aae59ce23b")

	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-rglpk@0.6.2:", type=("build", "run"))
	depends_on("r-sm@2.2.5.4:", type=("build", "run"))
	depends_on("r-transport@0.8.1:", type=("build", "run"))
