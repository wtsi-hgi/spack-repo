# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFma(RPackage):
	"""Data Sets from "Forecasting: Methods and Applications" by
Makridakis, Wheelwright & Hyndman (1998)

	All data sets from "Forecasting: methods and applications" by Makridakis, Wheelwright & Hyndman (Wiley, 3rd ed., 1998) <https://robjhyndman.com/forecasting/>.
	"""
	
	homepage = "https://pkg.robjhyndman.com/fma/"
	cran = "fma" 

	version("2.5", md5="cbca6ceaa58ddbf901677108a14e1677")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forecast@8.1:", type=("build", "run"))
