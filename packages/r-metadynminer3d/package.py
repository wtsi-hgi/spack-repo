# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetadynminer3d(RPackage):
	"""Tools to Read, Analyze and Visualize Metadynamics 3D HILLS Files
from 'Plumed'

	Metadynamics is a state of the art biomolecular simulation technique.
  'Plumed' Tribello, G.A. et al. (2014) <doi:10.1016/j.cpc.2013.09.018> program makes
  it possible to perform metadynamics using various simulation codes. The results of
  metadynamics done in 'Plumed' can be analyzed by 'metadynminer'. The package
  'metadynminer' reads 1D and 2D metadynamics hills files from 'Plumed' package.
  As an addendum, 'metadynaminer3d' is used to visualize 3D hills. It uses
  a fast algorithm by Hosek, P. and Spiwok, V. (2016) <doi:10.1016/j.cpc.2015.08.037>
  to calculate a free energy surface from hills. Minima can be located and plotted on
  the free energy surface. Free energy surfaces and minima can be plotted to produce
  publication quality images.
	"""
	
	homepage = "https://metadynamics.cz/metadynminer3d/"
	cran = "metadynminer3d" 

	version("0.0.2", md5="ec293fd3fa549d57d6eebc2eff7aba50")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-metadynminer", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
