# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmpd(RPackage):
	"""An Algorithm for Automatic Peak Detection in Noisy Periodic and
Quasi-Periodic Signals

	A method for automatic detection of peaks in noisy periodic and quasi-periodic signals. This method, called automatic multiscale-based peak detection (AMPD), is based on the calculation and analysis of the local maxima scalogram, a matrix comprising the scale-dependent occurrences of local maxima.
     For further information see  <doi:10.3390/a5040588>.
	"""
	
	cran = "ampd" 

	version("0.2", md5="68657018572ad734fec48fa831dedf07")

	depends_on("r@3.2:", type=("build", "run"))
