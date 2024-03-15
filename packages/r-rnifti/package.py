# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnifti(RPackage):
	"""Fast R and C++ Access to NIfTI Images

	Provides very fast read and write access to images stored in the
    NIfTI-1, NIfTI-2 and ANALYZE-7.5 formats, with seamless synchronisation
    of in-memory image objects between compiled C and interpreted R code. Also
    provides a simple image viewer, and a C/C++ API that can be used by other
    packages. Not to be confused with 'RNiftyReg', which performs image
    registration and applies spatial transformations.
	"""
	
	homepage = "https://github.com/jonclayden/RNifti"
	cran = "RNifti" 

	version("1.6.1", md5="95509945ea75a397a90d4d0b808d629d")

	depends_on("r-rcpp", type=("build", "run"))
