# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlstools(RPackage):
	"""Tools for Nonlinear Regression Analysis

	Several tools for assessing the quality of fit of a gaussian nonlinear model are provided.
	"""
	
	homepage = "https://github.com/lbbe-software/nlstools"
	cran = "nlstools" 

	version("2.1-0", md5="b13f76b09a314904ef6599d395af2f87")

