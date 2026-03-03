# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtephra(RPackage):
	"""Tephra Transport Modeling

	Models and displays tephra transport through custom (windy, turbulent, heterogeneous) atmosphere over custom topography. Includes a Lagrangian (particle-tracking) tephra transport model and a function to save snapshots of model as png files.
	"""
	
	cran = "rTephra" 

	version("0.1", md5="594c5b02ef9aebbc949d1b157641f9fe")

	depends_on("r@3:", type=("build", "run"))
