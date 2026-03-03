# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDensitr(RPackage):
	"""Analysing Density Profiles from Resistance Drilling of Trees

	Provides various tools for analysing density profiles
    obtained by resistance drilling. It can load individual or
    multiple files and trim the starting and ending part of each
    density profile. Tools are also provided to trim profiles
    manually, to remove the trend from measurements using several
    methods, to plot the profiles and to detect tree rings
    automatically. Written with a focus on forestry use of resistance
    drilling in standing trees.
	"""
	
	homepage = "https://github.com/krajnc/densitr"
	cran = "densitr" 

	version("0.2", md5="300e8283f890566740a82cb6bb00a06b")

	depends_on("r-changepoint@2.2.2:", type=("build", "run"))
