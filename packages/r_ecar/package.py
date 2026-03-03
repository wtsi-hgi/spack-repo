# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcar(RPackage):
	"""Eigenvalue CAR Models

	Fits Leroux model in spectral domain to estimate causal spatial effect as detailed in 
             Guan, Y; Page, G.L.; Reich, B.J.; Ventrucci, M.; Yang, S; (2020) <arXiv:2012.11767>.  
             Both the parametric and semi-parametric models are available.  The semi-parametric model 
             relies on 'INLA'.  The 'INLA' package can be obtained from <https://www.r-inla.org/>.
	"""
	
	homepage = "https://github.com/gpage2990/eCAR"
	cran = "eCAR" 

	version("0.1.2", md5="70cc1aa1d2b1517bddd6a4c088e4b9ef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
