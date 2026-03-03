# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmetrics(RPackage):
	"""Machine Learning Evaluation Metrics

	A collection of evaluation metrics, including loss, score and
    utility functions, that measure regression, classification and ranking performance.
	"""
	
	homepage = "http://github.com/yanyachen/MLmetrics"
	cran = "MLmetrics" 

	version("1.1.1", md5="91a1d321ad2b978a265443297f90bfb7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
