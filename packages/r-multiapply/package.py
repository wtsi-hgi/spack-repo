# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiapply(RPackage):
	"""Apply Functions to Multiple Multidimensional Arrays or Vectors

	The base apply function and its variants, as well as the related
    functions in the 'plyr' package, typically apply user-defined functions to a
    single argument (or a list of vectorized arguments in the case of mapply). The
    'multiApply' package extends this paradigm with its only function, Apply, which
    efficiently applies functions taking one or a list of multiple unidimensional
    or multidimensional arrays (or combinations thereof) as input. The input
    arrays can have different numbers of dimensions as well as different dimension
    lengths, and the applied function can return one or a list of unidimensional or
    multidimensional arrays as output. This saves development time by preventing the
    R user from writing often error-prone and memory-inefficient loops dealing with
    multiple complex arrays. Also, a remarkable feature of Apply is the transparent
    use of multi-core through its parameter 'ncores'. In contrast to the base apply
    function, this package suggests the use of 'target dimensions' as opposite
    to the 'margins' for specifying the dimensions relevant to the function to be
    applied.
	"""
	
	homepage = "https://earth.bsc.es/gitlab/ces/multiApply"
	cran = "multiApply" 

	version("2.1.4", md5="e03f80c2439e0e59c4d8e81a91f39fdc")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
