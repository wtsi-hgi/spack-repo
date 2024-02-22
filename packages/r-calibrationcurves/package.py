# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalibrationcurves(RPackage):
	"""Calibration Performance

	Plots calibration curves and computes statistics for assessing calibration performance. See De Cock Campo (2023) <arXiv:2309.08559> and Van Calster et al. (2016) <doi:10.1016/j.jclinepi.2015.12.005>.
	"""
	
	homepage = "https://bavodc.github.io/websiteCalibrationCurves/"
	cran = "CalibrationCurves" 

	version("2.0.0", md5="e298f0fd5949a34d24a34631b58fe095")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-bookdown", type=("build", "run"))
