# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlrcpo(RPackage):
	"""Composable Preprocessing Operators and Pipelines for Machine
Learning

	Toolset that enriches 'mlr' with a diverse set of preprocessing
    operators. Composable Preprocessing Operators ("CPO"s) are first-class
    R objects that can be applied to data.frames and 'mlr' "Task"s to modify
    data, can be attached to 'mlr' "Learner"s to add preprocessing to machine
    learning algorithms, and can be composed to form preprocessing pipelines.
	"""
	
	homepage = "https://github.com/mlr-org/mlrCPO"
	cran = "mlrCPO" 

	version("0.3.7-7", md5="0a3dce44a0ec73f70722db692cc7d980")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-paramhelpers@1.10:", type=("build", "run"))
	depends_on("r-mlr@2.12:", type=("build", "run"))
	depends_on("r-bbmisc@1.11:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-checkmate@1.8.3:", type=("build", "run"))
	depends_on("r-backports@1.1:", type=("build", "run"))
