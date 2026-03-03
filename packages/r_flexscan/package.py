# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexscan(RPackage):
	"""Flexible Scan Statistics

	An easy way to conduct flexible scan.
    Monte-Carlo method is used to test the spatial clusters given the cases, population, and shapefile.
    A table with formal style and a map with clusters are included in the result report.
    The method can be referenced at: Toshiro Tango and Kunihiko Takahashi (2005) <doi:10.1186/1476-072X-4-11>.
	"""
	
	cran = "FlexScan" 

	version("0.2.2", md5="50b092352f4a1e9407f3140de33bac05")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-smerc", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
