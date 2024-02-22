# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeostats(RPackage):
	"""An Introduction to Statistics for Geoscientists

	A collection of datasets and simplified functions for an introductory (geo)statistics module at University College London. Provides functionality for compositional, directional and spatial data, including ternary diagrams, Wulff and Schmidt stereonets, and ordinary kriging interpolation. Implements logistic and (additive and centred) logratio transformations. Computes vector averages and concentration parameters for the von-Mises distribution. Includes a collection of natural and synthetic fractals, and a simulator for deterministic chaos using a magnetic pendulum example. The main purpose of these functions is pedagogical. Researchers can find more complete alternatives for these tools in other packages such as 'compositions', 'robCompositions', 'sp', 'gstat' and 'RFOC'. All the functions are written in plain R, with no compiled code and a minimal number of dependencies. Theoretical background and worked examples are available at <https://tinyurl.com/UCLgeostats/>.
	"""
	
	homepage = "https://github.com/pvermees/geostats/"
	cran = "geostats" 

	version("1.6", md5="aa8ec9d906dfee1cc36ff1db219e0d95")

	depends_on("r@3.5:", type=("build", "run"))
