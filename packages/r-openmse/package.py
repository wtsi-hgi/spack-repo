# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenmse(RPackage):
	"""Easily Install and Load the 'openMSE' Packages

	The 'openMSE' package is designed for building operating models, 
    doing simulation modelling and management strategy evaluation for fisheries.
    'openMSE' is an umbrella package for the 'MSEtool' (Management Strategy Evaluation
    toolkit), 'DLMtool' (Data-Limited Methods toolkit), and 
    SAMtool (Stock Assessment Methods toolkit) packages. By loading and installing
    'openMSE', users have access to the full functionality contained within
    these packages. Learn more about 'openMSE' at <https://openmse.com/>.
	"""
	
	homepage = "https://openmse.com/"
	cran = "openMSE" 

	version("1.0.0", md5="cc5a66858278af6888c6181a18b52bbf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-msetool@3:", type=("build", "run"))
	depends_on("r-dlmtool@6:", type=("build", "run"))
	depends_on("r-samtool", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
