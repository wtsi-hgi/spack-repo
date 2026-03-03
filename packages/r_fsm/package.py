# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsm(RPackage):
	"""Finite Selection Model

	Randomized and balanced allocation of units to treatment groups using the Finite Selection Model (FSM). The FSM was originally proposed and developed at the RAND corporation by Carl Morris to enhance the experimental design for the now famous Health Insurance Experiment. See Morris (1979) <doi:10.1016/0304-4076(79)90053-8> for details on the original version of the FSM.
	"""
	
	cran = "FSM" 

	version("1.0.0", md5="599b9ada882d3eadaa2ed1b91d44f0fb")

	depends_on("r@3.5:", type=("build", "run"))
