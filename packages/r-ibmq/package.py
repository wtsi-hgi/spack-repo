# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbmq(RPackage):
	"""integrated Bayesian Modeling of eQTL data

	integrated Bayesian Modeling of eQTL data
	"""
	
	homepage = "http://www.rglab.org"
	bioc = "iBMQ"

	version("1.48.0", commit="a3a62fb0903ec43b6beb8cf3c8d838f06a3d0e80")
	version("1.42.0", commit="53c04e432c4af59b2482ea71f912e101fb240ac2")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biobase@2.16:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.2:", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
	depends_on("openmp", type=("build", "link", "run"))
