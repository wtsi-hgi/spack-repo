# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetadynminer(RPackage):
	"""Tools to Read, Analyze and Visualize Metadynamics HILLS Files
from 'Plumed'

	Metadynamics is a state of the art biomolecular simulation technique.
  'Plumed' Tribello, G.A. et al. (2014) <doi:10.1016/j.cpc.2013.09.018> program makes
  it possible to perform metadynamics using various simulation codes. The results of
  metadynamics done in 'Plumed' can be analyzed by 'metadynminer'. The package
  'metadynminer' reads 1D and 2D metadynamics hills files from 'Plumed' package.
  It uses a fast algorithm by Hosek, P. and Spiwok, V. (2016) <doi:10.1016/j.cpc.2015.08.037>
  to calculate a free energy surface from hills. Minima can be located and plotted on
  the free energy surface. Transition states can be analyzed by Nudged Elastic Band
  method by Henkelman, G. and Jonsson, H. (2000) <doi:10.1063/1.1323224>. Free energy
  surfaces, minima and transition paths can be plotted to produce publication quality
  images.
	"""
	
	homepage = "https://metadynamics.cz/metadynminer/"
	cran = "metadynminer" 

	version("0.1.7", md5="45a8de3b786d19878c241c0154254932")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
