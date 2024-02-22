# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR3pg(RPackage):
	"""Simulating Forest Growth using the 3-PG Model

	Provides a flexible and easy-to-use interface for the Physiological Processes Predicting Growth (3-PG) model written in Fortran. The r3PG serves as a flexible and easy-to-use interface for the 3-PGpjs (monospecific, evenaged and evergreen forests) described in Landsberg & Waring (1997) <doi:10.1016/S0378-1127(97)00026-1> and the 3-PGmix (deciduous, uneven-aged or mixed-species forests) described in Forrester & Tang (2016) <doi:10.1016/j.ecolmodel.2015.07.010>.
	"""
	
	homepage = "https://github.com/trotsiuk/r3PG"
	cran = "r3PG" 

	version("0.1.6", md5="8c83120b92093feb5606d093c4aab246")

	depends_on("r@3.5:", type=("build", "run"))
