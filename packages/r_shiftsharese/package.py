# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShiftsharese(RPackage):
	"""Inference in Regressions with Shift-Share Structure

	Provides confidence intervals in least-squares regressions when the
  variable of interest has a shift-share structure, and in instrumental
  variables regressions when the instrument has a shift-share structure. The
  confidence intervals implement the AKM and AKM0 methods developed in Adão,
  Kolesár, and Morales (2019) <doi:10.1093/qje/qjz025>.
	"""
	
	homepage = "https://github.com/kolesarm/ShiftShareSE"
	cran = "ShiftShareSE" 

	version("1.1.0", md5="42344934fb4f239f3bc58734035cc4ab")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
