# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpp3(RPackage):
	"""Data for "Forecasting: Principles and Practice" (3rd Edition)

	
    All data sets required for the examples and exercises in the book
    "Forecasting: principles and practice" by Rob J Hyndman and George Athanasopoulos
    <https://OTexts.com/fpp3/>.  All packages required to run the examples are also
    loaded.
	"""
	
	homepage = "https://github.com/robjhyndman/fpp3package"
	cran = "fpp3" 

	version("0.5", md5="5017a89f8752e0f950e5d7eea362d761", url="https://cran.r-project.org/src/contrib/fpp3_0.5.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.4:", type=("build", "run"))
	depends_on("r-fable@0.3:", type=("build", "run"))
	depends_on("r-fabletools@0.3:", type=("build", "run"))
	depends_on("r-feasts@0.1.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-tsibble@0.9.3:", type=("build", "run"))
	depends_on("r-tsibbledata@0.2:", type=("build", "run"))
