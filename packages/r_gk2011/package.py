# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGk2011(RPackage):
	"""Gaines and Kuklinski (2011) Estimators for Hybrid Experiments

	Implementations of the treatment effect estimators for hybrid (self-selection) experiments, as developed by Brian J. Gaines and James H. Kuklinski, (2011), "Experimental Estimation of Heterogeneous Treatment Effects Related to Self-Selection," American Journal of Political Science 55(3): 724-736.
	"""
	
	homepage = "https://github.com/leeper/GK2011"
	cran = "GK2011" 

	version("0.1.3", md5="123e2f88ef6eea234f6daf3d3b83ccb0", url="https://cran.r-project.org/src/contrib/GK2011_0.1.3.tar.gz")

