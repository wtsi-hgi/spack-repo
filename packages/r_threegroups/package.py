# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreegroups(RPackage):
	"""ML Estimator for Baseline-Placebo-Treatment (Three-Group)
Experiments

	Implements the Maximum Likelihood estimator for baseline, placebo, and treatment groups (three-group) experiments with non-compliance proposed by Gerber, Green, Kaplan, and Kern (2010).
	"""
	
	cran = "ThreeGroups" 

	version("0.21", md5="1a5ac5d24d0d5cbbbd025ca36e0c8ad6")

