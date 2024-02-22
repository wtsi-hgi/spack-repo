# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConconianaerobicthresholdtest(RPackage):
	"""Conconi Estimate of Anaerobic Threshold from a TCX File

	Analyzes data from a Conconi et al. (1996) <doi:10.1055/s-2007-972887>
    treadmill fitness test where speed is augmented by a constant amount every
    set number of seconds to estimate the anaerobic (lactate) threshold speed
    and heart rate. It reads a TCX file, allows optional removal observations
    from before and after the actual test, fits a change-point linear model
    where the change-point is the estimate of the lactate threshold, and plots
    the data points and fit model. Details of administering the fitness test are
    provided in the package vignette. Functions work by default for Garmin
    Connect TCX exports but may require additional data preparation for heart
    rate, time, and speed data from other sources.
	"""
	
	homepage = "https://github.com/waldronlab/ConconiAnaerobicThresholdTest"
	cran = "ConconiAnaerobicThresholdTest" 

	version("1.0.0", md5="3e28d2239bca1bfc307723a9dc158ad2")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tracker", type=("build", "run"))
	depends_on("r-sizer", type=("build", "run"))
