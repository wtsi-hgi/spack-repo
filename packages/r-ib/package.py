# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIb(RPackage):
	"""Bias Correction via Iterative Bootstrap

	An implementation of the iterative bootstrap procedure of 
    Kuk (1995) <doi:10.1111/j.2517-6161.1995.tb02035.x> to correct the estimation bias of a fitted model object. This
    procedure has better bias correction properties than the 
    bootstrap bias correction technique.
	"""
	
	homepage = "https://github.com/SMAC-Group/ib/"
	cran = "ib" 

	version("0.2.0", md5="c2bcfb2117f90cc5870f92bc6d026f9d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
