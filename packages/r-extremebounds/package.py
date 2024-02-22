# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtremebounds(RPackage):
	"""Extreme Bounds Analysis (EBA)

	An implementation of Extreme Bounds Analysis (EBA), a global sensitivity analysis that examines the robustness of determinants in regression models. The package supports both Leamer's and Sala-i-Martin's versions of EBA, and allows users to customize all aspects of the analysis.
	"""
	
	cran = "ExtremeBounds" 

	version("0.1.7", md5="63d9876c9427a59f0382d861c4e7f570")

	depends_on("r-formula", type=("build", "run"))
