# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeteoevt(RPackage):
	"""Computation and Visualization of Energetic and Vortical
Atmospheric Quantities

	Energy-Vorticity theory (EVT) is the fundamental theory to describe processes in the atmosphere by combining conserved quantities from hydrodynamics and thermodynamics. The package 'meteoEVT' provides functions to calculate many energetic and vortical quantities, like potential vorticity, Bernoulli function and dynamic state index (DSI) [e.g. Weber and Nevir, 2008, <doi:10.1111/j.1600-0870.2007.00272.x>], for given gridded data, like ERA5 reanalyses. These quantities can be studied directly or can be used for many applications in meteorology, e.g., the objective identification of atmospheric fronts. For this purpose, separate function are provided that allow the detection of fronts based on the thermic front parameter [Hewson, 1998, <doi:10.1017/S1350482798000553>], the F diagnostic [Parfitt et al., 2017, <doi:10.1002/2017GL073662>] and the DSI [Mack et al., 2022, <arXiv:2208.11438>].
	"""
	
	homepage = "https://github.com/noctiluc3nt/meteoEVT"
	cran = "meteoEVT" 

	version("0.1.0", md5="caa928e1f226066f150ee0acbe3e85d5")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
