# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REhof(RPackage):
	"""Extended HOF (Huisman-Olff-Fresco) Models

	Extended and enhanced hierarchical logistic regression models (called Huisman-Olff-Fresco in biology, see Huisman et al. 1993 Journal of Vegetation Science <doi:10.1111/jvs.12050>) models. Response curves along one-dimensional gradients including no response, monotone, plateau, unimodal and bimodal models. 
	"""
	
	cran = "eHOF" 

	version("1.15", md5="92ab687b622d296718669c21c3a9cafc")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
