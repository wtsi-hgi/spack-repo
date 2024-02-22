# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRseedcalc(RPackage):
	"""Estimating the Proportion of Genetically Modified Seeds in
Seedlots via Multinomial Group Testing

	Estimate the percentage of seeds in a seedlot that contain stacks
    of genetically modified traits.  Estimates are calculated using a
    multinomial group testing model with maximum likelihood estimation of the
    parameters.
	"""
	
	cran = "rseedcalc" 

	version("1.3", md5="de7ef8a3dd353787cd7c95e984b023fe")

