# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAscotracer(RPackage):
	"""Simulate the Spread of Ascochyta Blight in Chickpea

	A spatiotemporal model that simulates the spread of Ascochyta
    blight in chickpea fields based on location-specific weather conditions.
    This model is adapted from a model developed by Diggle et al. (2002)
   <doi:10.1094/PHYTO.2002.92.10.1110> for simulating the spread of anthracnose
   in a lupin field.
	"""
	
	homepage = "https://github.com/IhsanKhaliq/ascotraceR"
	cran = "ascotraceR" 

	version("0.0.1", md5="65300b2fe4beb25201e9971987ff8426")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9.2:", type=("build", "run"))
	depends_on("r-lutz@0.3.1:", type=("build", "run"))
	depends_on("r-circular@0.4.93:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
