# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConstants(RPackage):
	"""Reference on Constants, Units and Uncertainty

	CODATA internationally recommended values of the fundamental
    physical constants, provided as symbols for direct use within the R language.
    Optionally, the values with uncertainties and/or units are also provided if
    the 'errors', 'units' and/or 'quantities' packages are installed.
    The Committee on Data for Science and Technology (CODATA) is an
    interdisciplinary committee of the International Council for Science which
    periodically provides the internationally accepted set of values of the
    fundamental physical constants. This package contains the "2018 CODATA"
    version, published on May 2019:
    Eite Tiesinga, Peter J. Mohr, David B. Newell, and Barry N. Taylor (2020)
    <https://physics.nist.gov/cuu/Constants/>.
	"""
	
	homepage = "https://github.com/r-quantities/constants"
	cran = "constants" 

	version("1.0.1", md5="cda07cdf0aa3e718eecef657dcdb96d3")

	depends_on("r@3.5:", type=("build", "run"))
