# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamilial(RPackage):
	"""Statistical Tests of Familial Hypotheses

	Provides functionality for testing familial hypotheses. Supports testing centers 
    belonging to the Huber family. Testing is carried out using the Bayesian bootstrap. One- and 
    two-sample tests are supported, as are directional tests. Methods for visualizing output are 
    provided.
	"""
	
	homepage = "https://github.com/ryan-thompson/familial"
	cran = "familial" 

	version("1.0.5", md5="f8d141b445d300dc498eaa7756545bae")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-depthproc", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
