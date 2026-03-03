# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDischarge(RPackage):
	"""Fourier Analysis of Discharge Data

	Computes discrete fast Fourier transform of river discharge data and the derived metrics.
  The methods are described in J. L. Sabo, D. M. Post (2008) <doi:10.1890/06-1340.1> and J. L. Sabo, A. Ruhi, G. W. Holtgrieve, V. Elliott, M. E. Arias, P. B. Ngor, T. A. Räsänsen, S. Nam (2017) <doi:10.1126/science.aao1053>.
	"""
	
	cran = "discharge" 

	version("1.0.0", md5="5849b47273ae77b3ab622d115359057b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
