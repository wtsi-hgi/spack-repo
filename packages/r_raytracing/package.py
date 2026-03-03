# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaytracing(RPackage):
	"""Rossby Wave Ray Tracing

	Rossby wave ray paths are traced from 
             a determined source, specified wavenumber, and direction
             of propagation. "raytracing" also works with a set of 
             experiments changing these parameters, making possible the
             identification of Rossby wave sources automatically. 
             The theory used here is based on classical studies, 
             such as Hoskins and Karoly (1981) <doi:10.1175/1520-0469(1981)038%3C1179:TSLROA%3E2.0.CO;2>,
             Karoly (1983) <doi:10.1016/0377-0265(83)90013-1>, 
             Hoskins and Ambrizzi (1993) <doi:10.1175/1520-0469(1993)050%3C1661:RWPOAR%3E2.0.CO;2>,
             and Yang and Hoskins (1996) <doi:10.1175/1520-0469(1996)053%3C2365:PORWON%3E2.0.CO;2>.
	"""
	
	homepage = "https://github.com/salvatirehbein/raytracing/"
	cran = "raytracing" 

	version("0.6.0", md5="0a0c802db1495ca2c75d7abebdb2d31b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
