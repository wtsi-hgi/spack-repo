# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexparamcurve(RPackage):
	"""Tools to Fit Flexible Parametric Curves

	Model selection tools and 'selfStart' functions to fit parametric curves in 'nls', 'nlsList' and 'nlme' frameworks.
	"""
	
	homepage = "https://pennstate.academia.edu:443/SteveOswald"
	cran = "FlexParamCurve" 

	version("1.5-6", md5="7d5216e20eb36a0ab72958d38685dac3")

	depends_on("r-nlme", type=("build", "run"))
