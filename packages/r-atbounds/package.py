# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtbounds(RPackage):
	"""Bounding Treatment Effects by Limited Information Pooling

	Estimation and inference methods for bounding average treatment effects (on the treated) that are valid under an unconfoundedness assumption. 
    The bounds are designed to be robust in challenging situations, for example, when the conditioning variables take on a large number of different values in the observed sample, or when the overlap condition is violated. 
    This robustness is achieved by only using limited "pooling" of information across observations. 
    For more details, see the paper by Lee and Weidner (2021), "Bounding Treatment Effects by Pooling Limited Information across Observations," <arXiv:2111.05243>.
	"""
	
	homepage = "https://github.com/ATbounds/ATbounds-r/"
	cran = "ATbounds" 

	version("0.1.0", md5="42a1422f6ce01ce196596fa502ee638a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
