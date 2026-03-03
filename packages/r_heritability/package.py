# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeritability(RPackage):
	"""Marker-Based Estimation of Heritability Using Individual Plant
or Plot Data

	Implements marker-based estimation of heritability when observations on genetically identical replicates are available. These can be either observations on individual plants or plot-level data in a field trial. Heritability can then be estimated using a mixed model for the individual plant or plot data. For comparison, also mixed-model based estimation using genotypic means and estimation of repeatability with ANOVA are implemented. For illustration the package contains several datasets for the model species Arabidopsis thaliana.
	"""
	
	cran = "heritability" 

	version("1.4", md5="59edcb0b31c933d4c2c6d50027efccbf")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass@3.1.20:", type=("build", "run"))
