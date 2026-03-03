# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtsad(RPackage):
	"""Online Time Series Anomaly Detectors

	Implements a set of online fault detectors for time-series, called: PEWMA see M. Carter
             et al. (2012) <doi:10.1109/SSP.2012.6319708>, SD-EWMA and TSSD-EWMA see H. Raza et al. 
             (2015) <doi:10.1016/j.patcog.2014.07.028>, KNN-CAD see E. Burnaev et al. (2016)
             <arXiv:1608.04585>, KNN-LDCD see V. Ishimtsev et al. (2017) <arXiv:1706.03412> and 
             CAD-OSE see M. Smirnov (2018) <https://github.com/smirmik/CAD>. The first three 
             algorithms belong to prediction-based techniques and the last three belong to 
             window-based techniques. In addition, the SD-EWMA and PEWMA algorithms are algorithms 
             designed to work in stationary environments, while the other four 
             are algorithms designed to work in non-stationary environments.
	"""
	
	homepage = "https://github.com/alaineiturria/otsad"
	cran = "otsad" 

	version("0.2.0", md5="485ca29292829574a98e48af5739791e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-sigmoid", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("python@3.0.1:", type=("build", "link", "run"))
