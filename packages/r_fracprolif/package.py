# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFracprolif(RPackage):
	"""Fraction Proliferation via a Quiescent Growth Model

	Functions for fitting data to a quiescent growth model,
        i.e. a growth process that involves members of the population
        who stop dividing or propagating.
	"""
	
	cran = "fracprolif" 

	version("1.0.7", md5="bed87c8aa44b365fbbb9fc9cd9a0945a")

	depends_on("r-emg@1.0.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
