# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVolumodel(RPackage):
	"""Modeling Species Distributions in Three Dimensions

	Facilitates modeling species' ecological niches and 
  geographic distributions based on occurrences and environments that 
  have a vertical as well as horizontal component, and projecting models 
  into three-dimensional geographic space. Working in three dimensions is 
  useful in an aquatic context when the organisms one wishes to model can 
  be found across a wide range of depths in the water column. The package
  also contains functions to automatically generate marine training
  model training regions using machine learning, and interpolate and smooth
  patchily sampled environmental rasters using thin plate splines.
  Davis Rabosky AR, Cox CL, Rabosky DL, Title PO, Holmes IA, Feldman A, McGuire JA (2016) <doi:10.1038/ncomms11484>.
  Nychka D, Furrer R, Paige J, Sain S (2021) <doi:10.5065/D6W957CT>.
  Pateiro-Lopez B, Rodriguez-Casal A (2022) <https://CRAN.R-project.org/package=alphahull>.
	"""
	
	homepage = "https://hannahlowens.github.io/voluModel/"
	cran = "voluModel" 

	version("0.2.1", md5="a15c7ac2244ca01b03d3f49e0479d970")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-modeva", type=("build", "run"))
	depends_on("r-rangebuilder@2:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
