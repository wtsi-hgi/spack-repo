# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRssa(RPackage):
	"""A Collection of Methods for Singular Spectrum Analysis

	Methods and tools for Singular Spectrum Analysis including decomposition,
             forecasting and gap-filling for univariate and multivariate time series.
             General description of the methods with many examples can be found in the book
             Golyandina (2018, <doi:10.1007/978-3-662-57380-8>).
             See 'citation("Rssa")' for details.
	"""
	
	homepage = "https://github.com/asl/rssa"
	cran = "Rssa" 

	version("1.0.5", md5="00692021da9b2a168014384d03e6a0af")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-svd@0.4:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("fftw@3.2:", type=("build", "link", "run"))
