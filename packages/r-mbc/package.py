# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbc(RPackage):
	"""Multivariate Bias Correction of Climate Model Outputs

	Calibrate and apply multivariate bias correction algorithms
    for climate model simulations of multiple climate variables. Three methods
    described by Cannon (2016) <doi:10.1175/JCLI-D-15-0679.1> and 
    Cannon (2018) <doi:10.1007/s00382-017-3580-6> are implemented —
    (i) MBC Pearson correlation (MBCp), (ii) MBC rank correlation (MBCr),
    and (iii) MBC N-dimensional PDF transform (MBCn) — as is the Rank
    Resampling for Distributions and Dependences (R2D2) method.
	"""
	
	cran = "MBC" 

	version("0.10-6", md5="097b23175f9e289e4686a93fd9b8c59f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
