# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpp2(RPackage):
	"""Data for "Forecasting: Principles and Practice" (2nd Edition)

	All data sets required for the examples and exercises
  in the book "Forecasting: principles and practice" (2nd ed, 2018)
  by Rob J Hyndman and George Athanasopoulos <https://otexts.com/fpp2/>.
  All packages required to run the examples are also loaded.
	"""
	
	homepage = "https://pkg.robjhyndman.com/fpp2-package/"
	cran = "fpp2" 

	version("2.5", md5="6f8cf630a5b21c52cbcbf5bc3cafae98", url="https://cran.r-project.org/src/contrib/fpp2_2.5.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli@1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-expsmooth", type=("build", "run"))
	depends_on("r-fma", type=("build", "run"))
	depends_on("r-forecast@8.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
