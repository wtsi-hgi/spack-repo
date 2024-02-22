# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmt(RPackage):
	"""Restricted Mean Time in Favor of Treatment

	Contains inferential and graphical routines for comparing two treatment arms in terms of the restricted mean time in favor of treatment.
	"""
	
	homepage = "https://sites.google.com/view/lmaowisc/"
	cran = "rmt" 

	version("1.0", md5="6f9c62b26d285d0f687b2764ceea862d")

	depends_on("r@2.10:", type=("build", "run"))
