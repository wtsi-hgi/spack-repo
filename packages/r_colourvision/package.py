# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColourvision(RPackage):
	"""Colour Vision Models

	Colour vision models, colour spaces and colour thresholds. Provides flexibility to build user-defined colour vision models for n number of photoreceptor types. Also includes Vorobyev & Osorio (1998) Receptor Noise Limited models <doi:10.1098/rspb.1998.0302>, Chittka (1992) colour hexagon <doi:10.1007/BF00199331>, and Endler & Mielke (2005) model <doi:10.1111/j.1095-8312.2005.00540.x>. Models have been extended to accept any number of photoreceptor types. 
	"""
	
	cran = "colourvision" 

	version("2.0.4", md5="b0f64749deecae288578d51bba134108")

	depends_on("r-matrix", type=("build", "run"))
