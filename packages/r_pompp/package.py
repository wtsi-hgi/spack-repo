# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPompp(RPackage):
	"""Presence-Only for Marked Point Process

	Inspired by Moreira and Gamerman (2022) <doi:10.1214/21-AOAS1569>,
    this methodology expands the idea by including Marks in the point process.
    Using efficient 'C++' code, the estimation is possible and made faster with
    'OpenMP' <https://www.openmp.org/> enabled computers. This package was
    developed under the project PTDC/MAT-STA/28243/2017, supported by
    Portuguese funds through the Portuguese Foundation for Science and
    Technology (FCT).
	"""
	
	cran = "pompp" 

	version("0.1.3", md5="658f08b86ef713136c4fea1c83a00e23")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-geor", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
