# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShellchron(RPackage):
	"""Builds Chronologies from Oxygen Isotope Profiles in Shells

	Takes as input a stable oxygen isotope (d18O) profile measured in growth direction (D)
	through a shell + uncertainties in both variables (d18O_err & D_err). It then models the seasonality
	in the d18O record by fitting a combination of a growth and temperature sine wave to year-length chunks of
	the data (see Judd et al., (2018) <doi:10.1016/j.palaeo.2017.09.034>). This modeling is carried out along a sliding window through the data and yields estimates of
	the day of the year (Julian Day) and local growth rate for each data point. Uncertainties in both modeling
	routine and the data itself are propagated and pooled to obtain a confidence envelope around the age of
	each data point in the shell. The end result is a shell chronology consisting of estimated ages of shell
	formation relative to the annual cycle with their uncertainties. All formulae in the package serve this
	purpose, but the user can customize the model (e.g. number of days in a year and the mineralogy of the
	shell carbonate) through input parameters.
	"""
	
	homepage = "https://github.com/nielsjdewinter/ShellChron"
	cran = "ShellChron" 

	version("0.4.0", md5="03d10716d6831270fdf9b740d6621467")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rtop@0.5.14:", type=("build", "run"))
	depends_on("r-zoo@1.8.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-ggpubr@0.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
