# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWttopsis(RPackage):
	"""Weighted Method for Multiple-Criteria Decision Making

	Evaluation of alternatives based on multiple criteria using weighted technique for Order preference by similarity to an ideal solution method. Reference: Hwang CL. (1981, ISBN:978-3-540-10558-9).
	"""
	
	cran = "WtTopsis" 

	version("1.0", md5="d49741d5eea698377433afe30e543a8b")

	depends_on("r@2.10:", type=("build", "run"))
