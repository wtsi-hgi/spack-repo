# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpina(RPackage):
	"""Structure Parameter Inference Approach

	Calculates constant structure parameters of endocrine homeostatic systems from equilibrium hormone concentrations. Methods and equations have been described in Dietrich et al. (2012) <doi:10.1155/2012/351864> and Dietrich et al. (2016) <doi:10.3389/fendo.2016.00057>.
	"""
	
	homepage = "http://spina.sf.net/"
	cran = "SPINA" 

	version("4.1.0", md5="4f09b256c7bf5f0b6f94c8fed1cc7819")

	depends_on("r@3:", type=("build", "run"))
