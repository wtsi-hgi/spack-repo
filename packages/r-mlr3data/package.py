# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3data(RPackage):
	"""Collection of Machine Learning Data Sets for 'mlr3'

	A small collection of interesting and educational machine
    learning data sets which are used as examples in the 'mlr3' book
    (<https://mlr3book.mlr-org.com>), the use case gallery
    (<https://mlr3gallery.mlr-org.com>), or in other examples. All data
    sets are properly preprocessed and ready to be analyzed by most
    machine learning algorithms.  Data sets are automatically added to the
    dictionary of tasks if 'mlr3' is loaded.
	"""
	
	homepage = "https://github.com/mlr-org/mlr3data"
	cran = "mlr3data" 

	version("0.7.0", md5="ea3d36be60f8c41d4846960dc8fe4c8f")

	depends_on("r@3.1:", type=("build", "run"))
