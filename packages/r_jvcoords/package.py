# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJvcoords(RPackage):
	"""Principal Component Analysis (PCA) and Whitening

	
  Provides functions to standardize and whiten data, and to perform
  Principal Component Analysis (PCA).  The main advantage of this
  package over alternatives like prcomp() is, that jvcoords makes it
  easy to convert (additional) data between the original and the
  transformed coordinates.  The package also provides a class coords,
  which can represent affine coordinate transformations.  This class
  forms the basis of the transformations provided by the package, but
  can also be used independently.  The implementation has been
  optimized to be of comparable speed (and sometimes even faster) than
  existing alternatives.
	"""
	
	homepage = "https://github.com/seehuhn/jvcoords"
	cran = "jvcoords" 

	version("1.0.3", md5="9c10d757249958601e198597afc1a359")

