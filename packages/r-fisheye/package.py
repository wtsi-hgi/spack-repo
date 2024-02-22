# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFisheye(RPackage):
	"""Transform Base Maps Using Log-Azimuthal Projection

	Base maps are transformed to focus on a specific location using an
    azimuthal logarithmic distance transformation.
	"""
	
	homepage = "https://github.com/riatelab/fisheye"
	cran = "fisheye" 

	version("0.2.0", md5="7fe527c1718ad763a00550b91af04fbb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
