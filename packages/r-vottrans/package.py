# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVottrans(RPackage):
	"""Voter Transition Analysis

	Calculates voter transitions comparing two elections, using the function solve.QP() in package 'quadprog'.
	"""
	
	cran = "vottrans" 

	version("1.0", md5="cfe65037ffd2c56da8e4db1b96ab6109")

	depends_on("r-quadprog", type=("build", "run"))
