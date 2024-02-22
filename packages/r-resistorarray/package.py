# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResistorarray(RPackage):
	"""Electrical Properties of Resistor Networks

	Electrical properties of resistor networks using matrix methods.
	"""
	
	homepage = "https://github.com/RobinHankin/ResistorArray.git"
	cran = "ResistorArray" 

	version("1.0-32", md5="493943d684f5627dbbf7898d73b1430c")

