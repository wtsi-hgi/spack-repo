# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRniftyreg(RPackage):
	"""Image Registration Using the 'NiftyReg' Library

	Provides an 'R' interface to the 'NiftyReg' image registration tools
    <https://github.com/KCL-BMEIS/niftyreg>. Linear and nonlinear registration
    are supported, in two and three dimensions.
	"""
	
	homepage = "https://github.com/jonclayden/RNiftyReg"
	cran = "RNiftyReg" 

	version("2.8.1", md5="556637d2c79bf428592c27e78ba1c974")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-ore", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
