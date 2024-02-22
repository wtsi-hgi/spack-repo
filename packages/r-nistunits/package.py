# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNistunits(RPackage):
	"""Fundamental Physical Constants and Unit Conversions from NIST

	Fundamental physical constants (Quantity, Value, Uncertainty, Unit) for 
    SI (International System of Units) and non-SI units, plus unit conversions
    Based on the data from NIST (National Institute of Standards and Technology, USA)
	"""
	
	cran = "NISTunits" 

	version("1.0.1", md5="5354e46703018bd47f18eecb311029dc")

	depends_on("r@2.7:", type=("build", "run"))
