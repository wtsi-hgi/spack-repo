# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RTruncreg(RPackage):
	"""Truncated Gaussian Regression Models

	Estimation of models for truncated Gaussian variables by maximum likelihood.
	"""
	
	homepage = "http://R-Forge.R-project.org/projects/truncreg/"
	cran = "truncreg" 

	version("0.2-5", md5="6ddc73494a349da69b23f859ffe89a54")

	depends_on("r@1.8.0:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
