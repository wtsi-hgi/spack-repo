# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcf(RPackage):
	"""Linear Combination Fitting

	Baseline correction, normalization and linear combination fitting (LCF) 
    of X-ray absorption near edge structure (XANES) spectra.
    The package includes data loading of .xmu files exported from 'ATHENA' (Ravel and Newville, 2005) <doi:10.1107/S0909049505012719>. 
    Loaded spectra can be background corrected and all standards can be fitted at once.
    Two linear combination fitting functions can be used:
    (1) fit_athena(): Simply fitting combinations of standards as in ATHENA, 
    (2) fit_float(): Fitting all standards with changing baseline correction and edge-step normalization parameters. 
	"""
	
	cran = "LCF" 

	version("1.7.0", md5="c1a7c28fb9e152179ee76339016e6224")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
