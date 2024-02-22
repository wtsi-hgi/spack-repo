# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdspcalibration(RPackage):
	"""Statistical Methods for Designing and Analyzing a Calibration
Study

	Provides statistical methods for the design and analysis of a calibration study, which aims for calibrating measurements using two different methods. The package includes sample size calculation, sample selection,  regression analysis with error-in measurements and change-point regression. The method is described in Tian, Durazo-Arvizu, Myers, et al. (2014) <DOI:10.1002/sim.6235>.
	"""
	
	cran = "VDSPCalibration" 

	version("1.0", md5="59d1fbdb2e14868e80dc3391c3e97b56")

