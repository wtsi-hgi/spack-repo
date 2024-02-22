# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpmi(RPackage):
	"""Mixed-Pair Mutual Information Estimators

	Uses a kernel smoothing approach to calculate Mutual Information
    for comparisons between all types of variables including continuous vs
    continuous, continuous vs discrete and discrete vs discrete. Uses a
    nonparametric bias correction giving Bias Corrected Mutual Information
    (BCMI). Implemented efficiently in Fortran 95 with OpenMP and suited to
    large genomic datasets.  
	"""
	
	homepage = "https://r-forge.r-project.org/projects/mpmi/"
	cran = "mpmi" 

	version("0.43.2.1", md5="05858a74af0888bfc700c2ca3c6c050c")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
