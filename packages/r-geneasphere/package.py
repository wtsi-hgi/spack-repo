# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneasphere(RPackage):
	"""Visualisation of Raw or Segmented Accelerometer Data

	Creates visualisations in two and three dimensions of simulated
    data based on detected segments or raw accelerometer data.
	"""
	
	cran = "GENEAsphere" 

	version("1.5.1", md5="6190c3dd23b4f7d798f63189c7214d84")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-genearead", type=("build", "run"))
