# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcmixed(RPackage):
	"""Mixed Effect Model with the Box-Cox Transformation

	Inference on the marginal model of the mixed effect model with 
    the Box-Cox transformation and on the model median differences between
    treatment groups for longitudinal randomized clinical trials. These 
    statistical methods are proposed by Maruo et al. (2017) 
    <doi:10.1002/sim.7279>.
	"""
	
	cran = "bcmixed" 

	version("0.1.4", md5="43374b44051090317a43dc8416601f82")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-nlme@3.1.131:", type=("build", "run"))
