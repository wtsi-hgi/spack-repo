# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinovisualfields(RPackage):
	"""Depth-Dependent Binocular Visual Fields Simulation

	Simulation and visualization depth-dependent integrated visual fields. Visual fields are measured monocularly at a single depth, yet real-life activities involve predominantly binocular vision at multiple depths. The package provides functions to simulate and visualize binocular visual field impairment in a depth-dependent fashion from monocular visual field results based on Ping Liu, Allison McKendrick, Anna Ma-Wyatt, Andrew Turpin (2019) <doi:10.1167/tvst.9.3.8>. At each location and depth plane, sensitivities are linearly interpolated from corresponding locations in monocular visual field and returned as the higher value of the two. Its utility is demonstrated by evaluating DD-IVF defects associated with 12 glaucomatous archetypes of 24-2 visual field pattern in the included 'shiny' apps. 
	"""
	
	homepage = "https://people.eng.unimelb.edu.au/aturpin/opi/index.html"
	cran = "binovisualfields" 

	version("0.1.1", md5="cfec2b9e44ff5a404a6d33926627d842")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
