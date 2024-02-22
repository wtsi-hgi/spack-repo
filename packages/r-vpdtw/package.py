# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVpdtw(RPackage):
	"""Variable Penalty Dynamic Time Warping

	Variable Penalty Dynamic Time Warping (VPdtw) for aligning chromatographic signals. With an appropriate penalty this method performs good alignment of chromatographic data without deforming the peaks (Clifford, D., Stone, G., Montoliu, I., Rezzi S., Martin F., Guy P., Bruce S., and Kochhar S.(2009) <doi:10.1021/ac802041e>; Clifford, D. and Stone, G. (2012) <doi:10.18637/jss.v047.i08>).
	"""
	
	homepage = "https://github.com/ethanbass/VPdtw/"
	cran = "VPdtw" 

	version("2.1-14", md5="079fab479fac5010e91a766860988eaa")

