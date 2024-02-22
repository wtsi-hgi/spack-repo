# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhrt(RPackage):
	"""Heart Rate Turbulence Analysis

	Methods to scan RR interval data for Premature Ventricular Complexes (PVCs) and parameterise and plot the resulting Heart Rate Turbulence (HRT). The methodology of HRT analysis is based on the original publication by Schmidt et al. <doi:10.1016/S0140-6736(98)08428-1> and extended with suggestions from <doi:10.1088/1361-6579/ab98b3>.
	"""
	
	cran = "RHRT" 

	version("1.0.1", md5="96447a583dd4ce58aa3d6af9caffc42d")

	depends_on("r@3.5:", type=("build", "run"))
