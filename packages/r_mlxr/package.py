# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlxr(RPackage):
	"""Simulation of Longitudinal Data

	Simulation and visualization of complex
    models for longitudinal data. The models are encoded using the model coding
    language 'Mlxtran' and automatically converted into C++ codes. 
    That allows one to implement very easily complex ODE-based models and complex 
    statistical models, including mixed effects models, for continuous, count, 
    categorical, and time-to-event data.
	"""
	
	homepage = "http://simulx.webpopix.org"
	cran = "mlxR" 

	version("4.2.0", md5="945571af1a66aed5dcd8a4f71858c00a")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
