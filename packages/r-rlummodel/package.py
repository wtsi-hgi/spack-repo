# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlummodel(RPackage):
	"""Solving Ordinary Differential Equations to Understand
Luminescence

	A collection of functions to simulate luminescence signals in quartz and Al2O3 based on published models.
	"""
	
	homepage = "https://CRAN.R-project.org/package=RLumModel"
	cran = "RLumModel" 

	version("0.2.10", md5="eaf27fe35c1716c366f5f0d6fbca8019")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-luminescence@0.9.18:", type=("build", "run"))
	depends_on("r-desolve@1.30:", type=("build", "run"))
	depends_on("r-khroma@1.8:", type=("build", "run"))
	depends_on("r-rcpp@1.0.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.400.2:", type=("build", "run"))
