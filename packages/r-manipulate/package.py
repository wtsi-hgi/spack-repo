# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManipulate(RPackage):
	"""Interactive Plots for RStudio

	Interactive plotting functions for use within RStudio.
  The manipulate function accepts a plotting expression and a set of
  controls (e.g. slider, picker, checkbox, or button) which are used
  to dynamically change values within the expression. When a value is
  changed using its corresponding control the expression is
  automatically re-executed and the plot is redrawn.
	"""
	
	cran = "manipulate" 

	version("1.0.1", md5="f1e4156797a07327020c28cc7e3318bf")

	depends_on("r@2.11.1:", type=("build", "run"))
