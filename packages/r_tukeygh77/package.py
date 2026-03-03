# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTukeygh77(RPackage):
	"""Tukey g-&-h Distribution

	Functions for density,
     cumulative density, quantile and
     simulation of Tukey g-and-h (1977)
     distributions. The quantile-based
     transformation (Hoaglin 1985
     <doi:10.1002/9781118150702.ch11>) and
     its reverse transformation, as well as
     the letter-value based estimates
     (Hoaglin 1985), are also provided.
	"""
	
	cran = "TukeyGH77" 

	version("0.1.1", md5="0d9fc7843f575a06b82bea6e9d0a4e3b", url="https://cran.r-project.org/src/contrib/TukeyGH77_0.1.1.tar.gz")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rstpm2", type=("build", "run"))
