# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmolt(RPackage):
	"""Graphic Visualization of the Birds' Molt

	Graphical visualization of the birds' molt to facilitate the creation of molting graph for passerines having 9 (Rmolt(data,9)) or 10 primaries (Rmolt(data,10)), and also only for the 10 first primaries (Rmolt(data,"10_0")).
	"""
	
	cran = "Rmolt" 

	version("1.0.0", md5="6d295d58736ab2e3f01989022358d150")

	depends_on("r@2.10:", type=("build", "run"))
