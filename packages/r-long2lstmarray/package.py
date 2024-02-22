# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLong2lstmarray(RPackage):
	"""Longitudinal Dataframes into Arrays for Machine Learning
Training

	An easy tool to transform 2D longitudinal data into 3D arrays suitable for 
  Long short-term memory neural networks training. The array output can be
  used by the 'keras' package. Long short-term memory neural networks are described
  in: Hochreiter, S., & Schmidhuber, J. (1997) <doi:10.1162/neco.1997.9.8.1735>.
	"""
	
	homepage = "https://github.com/luisgarcez11/long2lstmarray"
	cran = "long2lstmarray" 

	version("0.2.0", md5="6bbda6666b747199f3d759548784dd0f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
