# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpsp(RPackage):
	"""Nonparametric Spatial Statistics

	Multidimensional nonparametric spatial (spatio-temporal) geostatistics.
    S3 classes and methods for multidimensional: linear binning,
    local polynomial kernel regression (spatial trend estimation), density and variogram estimation.
    Nonparametric methods for simultaneous inference on both spatial trend
    and variogram functions (for spatial processes).
    Nonparametric residual kriging (spatial prediction).
    For details on these methods see, for example, Fernandez-Casal and Francisco-Fernandez (2014) 
    <doi:10.1007/s00477-013-0817-8> or Castillo-Paez et al. (2019) <doi:10.1016/j.csda.2019.01.017>.
	"""
	
	homepage = "https://rubenfcasal.github.io/npsp/"
	cran = "npsp" 

	version("0.7-13", md5="1871078bd19cb4a53c6c663e7f9d7a12")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
