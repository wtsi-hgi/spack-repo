# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvynom(RPackage):
	"""Nomograms for Right-Censored Outcomes from Survey Designs

	Builds, evaluates and validates a nomogram with survey data
    and right-censored outcomes. As described in Capanu (2015)
    <doi:10.18637/jss.v064.c01>, the package contains functions to create
    the nomogram, validate it using bootstrap, as well as produce the
    calibration plots.
	"""
	
	homepage = "https://github.com/MSKCC-Epi-Bio/SvyNom"
	cran = "SvyNom" 

	version("1.2", md5="3569f234ac18ac02718dabefe07468ab")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
