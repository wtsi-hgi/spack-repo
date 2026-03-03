# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNvctr(RPackage):
	"""The n-vector Approach to Geographical Position Calculations
using an Ellipsoidal Model of Earth

	The n-vector framework uses the normal vector to
    the Earth ellipsoid (called n-vector) as a non-singular position
    representation that turns out to be very convenient for practical
    position calculations.  The n-vector is simple to use and gives exact
    answers for all global positions, and all distances, for both
    ellipsoidal and spherical Earth models.  This package is a translation
    of the 'Matlab' library from FFI, the Norwegian Defence Research
    Establishment, as described in Gade (2010)
    <doi:10.1017/S0373463309990415>.
	"""
	
	homepage = "https://github.com/euctrl-pru/nvctr"
	cran = "nvctr" 

	version("0.1.4", md5="fe9b77eaf16ef2b94872bd18a35f09f1")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
