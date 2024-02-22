# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmpiricalcalibration(RPackage):
	"""Routines for Performing Empirical Calibration of Observational
Study Estimates

	Routines for performing empirical calibration of observational
  study estimates. By using a set of negative control hypotheses we can
  estimate the empirical null distribution of a particular observational
  study setup. This empirical null distribution can be used to compute a
  calibrated p-value, which reflects the probability of observing an
  estimated effect size when the null hypothesis is true taking both random
  and systematic error into account. A similar approach can be used to
  calibrate confidence intervals, using both negative and positive controls. 
  For more details, see Schuemie et al. (2013) <doi:10.1002/sim.5925> and
  Schuemie et al. (2018) <doi:10.1073/pnas.1708282114>.
	"""
	
	homepage = "https://ohdsi.github.io/EmpiricalCalibration/"
	cran = "EmpiricalCalibration" 

	version("3.1.2", md5="6c2c4bbaed9ac83bcf5b18151e851aff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
