# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPupaim(RPackage):
	"""A Collection of Physical and Chemical Adsorption Isotherm Models

	The PUPAIM R package can generally fit any adsorption experimental data to any of the 55 available adsorption isotherm models - 32 nonlinear models and 23 linear models. This package provides parameter estimation, model accuracy analysis, model error analysis, and adsorption plot created using the package 'ggplot2'. This package will help the users for a much easier way of adsorption model data fitting.
	"""
	
	cran = "PUPAIM" 

	version("0.3.1", md5="7779e5dec164b8b3e82354e96a3f6a2d")

	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
