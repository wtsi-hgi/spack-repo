# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdi(RPackage):
	"""Volumetric Analysis using Graphic Double Integration

	Tools implementing an automated version of the graphic double integration technique (GDI) for volume implementation, and some other related utilities for paleontological image-analysis. GDI was first employed by Jerison (1973) <ISBN:9780323141086> and Hurlburt (1999) <doi:10.1080/02724634.1999.10011145> and is primarily used for volume or mass estimation of (extinct) animals. The package 'gdi' aims to make this technique as convenient and versatile as possible. The core functions of 'gdi' provide utilities for automatically measuring diameters from digital silhouettes provided as image files and calculating volume via graphic double integration with simple elliptical, superelliptical (following Motani 2001 <doi:10.1666/0094-8373(2001)027%3C0735:EBMFST%3E2.0.CO;2>) or complex cross-sectional models. Additionally, the package provides functions for estimating the center of mass position (COM), the moment of inertia (I) for 3D shapes and the second moment of area (Ix) of 2D cross-sections, as well as for visualization of results.
	"""
	
	cran = "gdi" 

	version("1.5.4", md5="7c399708249ce3dba284391ae48a142a")

	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
