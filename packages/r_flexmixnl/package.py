# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexmixnl(RPackage):
	"""Finite Mixture Modeling of Generalized Nonlinear Models

	The fitting of mixtures of generalized nonlinear models is implemented as an extension of the existing package 'flexmix'. 
	"""
	
	cran = "flexmixNL" 

	version("0.0.1", md5="0dd0755fed6b158676fbeedf09b79d49")

	depends_on("r-flexmix@2.3.14:", type=("build", "run"))
	depends_on("r-gnm@1.0.8:", type=("build", "run"))
