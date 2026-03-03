# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircular(RPackage):
	"""Circular Statistics

	Circular Statistics, from "Topics in circular Statistics" (2001) S. Rao Jammalamadaka and A. SenGupta, World Scientific.
	"""
	
	cran = "circular" 

	version("0.5-0", md5="30ab87f09139540dec4dfdd933c5aff9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
