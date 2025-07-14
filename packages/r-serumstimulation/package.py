# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSerumstimulation(RPackage):
	"""serumStimulation is a data package which is used by examples in package pcaGoPromoter

	Contains 13 micro array data results from a serum stimulation experiment
	"""
	
	bioc = "serumStimulation"

	version("1.44.0", commit="df629e271f9b6d5345aec94f91daacd85950e239")
	version("1.38.0", commit="22299f557735d94027449d8f119a9c01fb50fdcd")

	depends_on("r@2.10:", type=("build", "run"))

