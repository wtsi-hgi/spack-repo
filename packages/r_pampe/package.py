# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPampe(RPackage):
	"""Implementation of the Panel Data Approach Method for Program
Evaluation

	Implements the Panel Data Approach Method for program evaluation as developed in Hsiao, Ching and Ki Wan (2012). pampe estimates the effect of an intervention by comparing the evolution of the outcome for a unit affected by an intervention or treatment to the evolution of the unit had it not been affected by the intervention.
	"""
	
	cran = "pampe" 

	version("1.1.2", md5="c4af42d7f6ee1b229dba3c866d445ca8")

	depends_on("r-leaps", type=("build", "run"))
