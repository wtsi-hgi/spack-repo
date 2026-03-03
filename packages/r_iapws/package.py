# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIapws(RPackage):
	"""Formulations of the International Association for the Properties
of Water and Steam

	Implementation of some of the formulations for the thermodynamic
	and transport properties released by the International Association for
	the Properties of Water and Steam (IAPWS). More specifically, the
	releases R1-76(2014), R5-85(1994), R6-95(2018), R7-97(2012), R8-97,
	R9-97, R10-06(2009), R11-07(2019), R12-08, R15-11, R16-17(2018),
	R17-20 and R18-21 at <http://iapws.org>.
	"""
	
	cran = "iapws" 

	version("1.1", md5="9346c4f3485185f2253cda6dd0210296")

	depends_on("r@3.2.2:", type=("build", "run"))
