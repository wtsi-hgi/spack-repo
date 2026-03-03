# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtakrig(RPackage):
	"""Area-to-Area Kriging

	Point-scale variogram deconvolution from irregular/regular spatial support according to Goovaerts, P., (2008) <doi: 10.1007/s11004-007-9129-1>; ordinary area-to-area (co)Kriging and area-to-point (co)Kriging.
	"""
	
	cran = "atakrig" 

	version("0.9.8.1", md5="432bd4455a21de0fd272db581200c929")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
