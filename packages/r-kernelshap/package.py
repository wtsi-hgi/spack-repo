# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernelshap(RPackage):
	"""Kernel SHAP

	Efficient implementation of Kernel SHAP, see Lundberg and Lee
    (2017), and Covert and Lee (2021)
    <http://proceedings.mlr.press/v130/covert21a>.  Furthermore, for up to
    14 features, exact permutation SHAP values can be calculated.  The
    package plays well together with meta-learning packages like
    'tidymodels', 'caret' or 'mlr3'.  Visualizations can be done using the
    R package 'shapviz'.
	"""
	
	homepage = "https://github.com/ModelOriented/kernelshap"
	cran = "kernelshap" 

	version("0.4.1", md5="b5b3a1bde8a874c4fff5d24094b722ff")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
