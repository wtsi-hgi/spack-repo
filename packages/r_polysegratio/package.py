# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolysegratio(RPackage):
	"""Simulate and Test Marker Dosage for Dominant Markers in
Autopolyploids

	Perform classic chi-squared tests and Ripol et al(1999)
             binomial confidence interval approach for autopolyploid
             dominant markers. Also, dominant markers may be generated
             for families of offspring where either one or both of the
             parents possess the marker. Missing values and
             misclassified markers may be generated at random.
	"""
	
	cran = "polySegratio" 

	version("0.2-5", md5="71396bac3b573ed7041b0e6cb9564dfa")

	depends_on("r-gdata", type=("build", "run"))
