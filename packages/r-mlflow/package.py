# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlflow(RPackage):
	"""Interface to 'MLflow'

	R interface to 'MLflow', open source platform for
    the complete machine learning life cycle, see <https://mlflow.org/>.
    This package supports installing 'MLflow', tracking experiments,
    creating and running projects, and saving and serving models.
	"""
	
	homepage = "https://github.com/mlflow/mlflow"
	cran = "mlflow" 

	version("2.11.1", md5="7ce56dca711af56912f1a3e568533392")
	version("2.10.2", md5="bec771c75bb3b4f2744d4ecec298c152")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-forge", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ini", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-swagger", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
