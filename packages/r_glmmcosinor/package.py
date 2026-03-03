# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmcosinor(RPackage):
	"""Fit a Cosinor Model Using a Generalised Mixed Modelling
Framework

	Allows users to fit a cosinor model using the 'glmmTMB' framework. 
    This extends on existing cosinor modelling packages, including 'cosinor' 
    and 'circacompare', by including a wide range of available link functions 
    and the capability to fit mixed models. The cosinor model is described by 
    Cornelissen (2014) <doi:10.1186/1742-4682-11-16>.
	"""
	
	homepage = "https://github.com/ropensci/GLMMcosinor"
	cran = "GLMMcosinor" 

	version("0.2.0", md5="b8774a3d543dc99275dbfa037dd6d717")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmmtmb", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
