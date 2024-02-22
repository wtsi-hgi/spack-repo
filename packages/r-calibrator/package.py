# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibrator(RPackage):
	"""Bayesian Calibration of Complex Computer Codes

	Performs Bayesian calibration of computer models as per
 Kennedy and O'Hagan 2001.  The package includes routines to find the
 hyperparameters and parameters; see the help page for stage1() for a
 worked example using the toy dataset.  A tutorial is provided in the
 calex.Rnw vignette; and a suite of especially simple one dimensional
 examples appears in inst/doc/one.dim/.
	"""
	
	homepage = "https://github.com/RobinHankin/calibrator.git"
	cran = "calibrator" 

	version("1.2-8", md5="0b033e73895fa33611b6d7b068db87d6")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-emulator@1.2.11:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
