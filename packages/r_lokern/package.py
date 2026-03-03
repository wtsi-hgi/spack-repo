# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLokern(RPackage):
	"""Kernel Regression Smoothing with Local or Global Plug-in
Bandwidth

	Kernel regression smoothing with adaptive local or global plug-in
	     bandwidth selection.
	"""
	
	homepage = "https://curves-etc.r-forge.r-project.org/"
	cran = "lokern" 

	version("1.1-10.1", md5="c9c624d48206203d261b3e84255bcd07")

	depends_on("r-sfsmisc@1.0.12:", type=("build", "run"))
