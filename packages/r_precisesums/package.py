# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecisesums(RPackage):
	"""Accurate Floating Point Sums and Products

	Most of the time floating point arithmetic does
  approximately the right thing.  When adding sums or having products
  of numbers that greatly differ in magnitude, the floating point
  arithmetic may be incorrect.  This package implements the Kahan
  (1965) sum <doi:10.1145/363707.363723>, Neumaier (1974) sum
  <doi:10.1002/zamm.19740540106>, pairwise-sum (adapted from 'NumPy',
  See Castaldo (2008) <doi:10.1137/070679946> for a discussion of
  accuracy), and arbitrary precision sum (adapted from the fsum in
  'Python' ; Shewchuk (1997)
  <https://people.eecs.berkeley.edu/~jrs/papers/robustr.pdf>).  In addition,
  products are changed to long double precision for accuracy, or
  changed into a log-sum for accuracy.
	"""
	
	homepage = "https://github.com/nlmixr2/PreciseSums"
	cran = "PreciseSums" 

	version("0.6", md5="392aa58af35a671a0c0daf1ec874d02b")

	depends_on("r@3.2:", type=("build", "run"))
