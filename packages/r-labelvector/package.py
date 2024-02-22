# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabelvector(RPackage):
	"""Label Attributes for Atomic Vectors

	Labels are a common construct in statistical software providing a 
  human readable description of a variable. While variable names are succinct,
  quick to type, and follow a language's naming conventions, labels may 
  be more illustrative and may use plain text and spaces. R does not provide
  native support for labels. Some packages, however, have made this feature
  available.  Most notably, the 'Hmisc' package provides labelling methods
  for a number of different object. Due to design decisions, these methods
  are not all exported, and so are unavailable for use in package development.
  The 'labelVector' package supports labels for atomic vectors in a light-weight
  design that is suitable for use in other packages.
	"""
	
	cran = "labelVector" 

	version("0.1.2", md5="ad69706c30f9670a7d1c1896164856d6")

	depends_on("r@2:", type=("build", "run"))
