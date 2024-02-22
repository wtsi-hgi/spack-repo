# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhrv(RPackage):
	"""Heart Rate Variability Analysis of ECG Data

	Allows users to import data files containing heartbeat	positions in the most broadly used formats, to remove outliers or points with unacceptable physiological values present in the time series, to plot HRV data, and to perform time domain, frequency domain and nonlinear HRV analysis. See Garcia et al. (2017) <DOI:10.1007/978-3-319-65355-6>.
	"""
	
	homepage = "http://rhrv.r-forge.r-project.org/"
	cran = "RHRV" 

	version("4.2.7", md5="3d13bf8468a9a754a3cbb03ada3669e3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-waveslim@1.6.4:", type=("build", "run"))
	depends_on("r-nonlineartseries@0.2.3:", type=("build", "run"))
	depends_on("r-lomb@1:", type=("build", "run"))
