# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcrtm(RPackage):
	"""Coupled Chain Radiative Transfer Models

	A set of radiative transfer models to quantitatively describe the absorption, reflectance and transmission of solar energy in vegetation, and model remotely sensed spectral signatures of vegetation at distinct spatial scales (leaf,canopy and stand). The main principle behind ccrtm is that many radiative transfer models can form a coupled chain, basically models that feed into each other in a linked chain (from leaf, to canopy, to stand, to atmosphere). It allows the simulation of spectral datasets in the solar spectrum (400-2500nm) using leaf models as PROSPECT5, 5b, and D which can be coupled with canopy models as 'FLIM', 'SAIL' and 'SAIL2'. Currently, only a simple atmospheric model ('skyl') is implemented. Jacquemoud et al 2008 provide the most comprehensive overview of these models <doi:10.1016/j.rse.2008.01.026>. 
	"""
	
	homepage = "https://github.com/MarcoDVisser/ccrtm"
	cran = "ccrtm" 

	version("0.1.6", md5="d1f8465b43706d71b2b3f612e8b53bc2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
