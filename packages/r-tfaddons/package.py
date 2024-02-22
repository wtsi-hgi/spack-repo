# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfaddons(RPackage):
	"""Interface to 'TensorFlow SIG Addons'

	'TensorFlow SIG Addons' <https://www.tensorflow.org/addons> is a repository 
             of community contributions that conform to well-established API patterns, 
             but implement new functionality not available in core 'TensorFlow'. 
             'TensorFlow' natively supports a large number of operators, layers, metrics, 
             losses, optimizers, and more. However, in a fast moving field like Machine Learning, 
             there are many interesting new developments that cannot be integrated into 
             core 'TensorFlow' (because their broad applicability is not yet clear, or 
             it is mostly used by a smaller subset of the community).
	"""
	
	homepage = "https://github.com/henry090/tfaddons"
	cran = "tfaddons" 

	version("0.10.0", md5="5834a327433392e299fb7cca18874909")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tensorflow", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-keras", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("py-tensorflow@2.0:", type=("build", "link", "run"))
