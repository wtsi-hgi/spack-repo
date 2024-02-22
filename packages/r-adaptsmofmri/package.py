# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptsmofmri(RPackage):
	"""Adaptive Smoothing of FMRI Data

	Adaptive smoothing functions for estimating the blood
    oxygenation level dependent (BOLD) effect by using functional Magnetic
    Resonance Imaging (fMRI) data, based on adaptive Gauss Markov random
    fields, for real as well as simulated data. The implemented models make 
    use of efficient Markov Chain Monte Carlo methods. Implemented methods 
    are based on the research developed by A. Brezger, L. Fahrmeir, A. 
    Hennerfeind (2007) <https://www.jstor.org/stable/4626770>.
	"""
	
	cran = "adaptsmoFMRI" 

	version("1.2", md5="a188d1ea21b4074a163f955c3e140a45")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-spatstat", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
