# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnthro(RPackage):
	"""Computation of the WHO Child Growth Standards

	Provides WHO Child Growth Standards (z-scores) with
             confidence intervals and standard errors around the
             prevalence estimates, taking into account complex sample designs.
             More information on the methods is
             available online:
             <https://www.who.int/tools/child-growth-standards>.
	"""
	
	homepage = "https://github.com/worldhealthorganization/anthro"
	cran = "anthro" 

	version("1.0.1", md5="664c3652524e1788361dec5d605fef5f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
