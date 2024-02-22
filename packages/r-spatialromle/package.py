# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialromle(RPackage):
	"""Robust Maximum Likelihood Estimation for Spatial Error Model

	Provides robust estimation for spatial error model to presence of outliers in the residuals. The classical estimation methods can be influenced by the presence of outliers in the data. We proposed a robust estimation approach based on the robustified likelihood equations for spatial error model (Vural Yildirim & Yeliz Mert Kantar (2020): Robust estimation approach for spatial error model, Journal of Statistical Computation and Simulation, <doi:10.1080/00949655.2020.1740223>).
	"""
	
	cran = "SpatialRoMLE" 

	version("0.1.0", md5="6147d9db24d3c8a63c4b32dddb3b15ec")

	depends_on("r@2.10:", type=("build", "run"))
