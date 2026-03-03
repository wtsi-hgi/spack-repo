# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrexselector(RPackage):
	"""T-Rex Selector: High-Dimensional Variable Selection & FDR
Control

	Performs fast variable selection in high-dimensional settings while controlling the 
    false discovery rate (FDR) at a user-defined target level. The package is based on the paper 
    Machkour, Muma, and Palomar (2022) <arXiv:2110.06048>.
	"""
	
	homepage = "https://github.com/jasinmachkour/TRexSelector"
	cran = "TRexSelector" 

	version("1.0.0", md5="0ca69edb15bc7dbff6ab1e01bb2f8b8b")
	version("0.0.1", md5="06ac7ab8dd79e3c3a3ec460d850c6f88")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tlars", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
