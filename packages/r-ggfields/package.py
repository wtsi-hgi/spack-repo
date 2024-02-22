# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfields(RPackage):
	"""Add Vector Field Layers to Ggplots

	Add vector field layers to ggplots. Ideal for visualising
    wind speeds, water currents, electric/magnetic fields, etc.
    Accepts data.frames simple features (sf) and spatiotemporal arrays (stars)
    objects as input. Vector fields are depicted as arrows starting at specified
    locations, and with specified angles and radii.
	"""
	
	homepage = "https://pepijn-devries.github.io/ggfields/"
	cran = "ggfields" 

	version("0.0.3", md5="48a7ab407a2886a99fa9aec204489624")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-rlang@1.1.2:", type=("build", "run"))
	depends_on("r-sf@1.0.15:", type=("build", "run"))
	depends_on("r-scales@1.3:", type=("build", "run"))
