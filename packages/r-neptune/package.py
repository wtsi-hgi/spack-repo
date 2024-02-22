# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeptune(RPackage):
	"""MLOps Metadata Store - Experiment Tracking and Model Registry
for Production Teams

	An interface to Neptune. A metadata store for MLOps, built for teams that run a lot of experiments.
    It gives you a single place to log, store, display, organize, compare, and query all your model-building metadata.
    Neptune is used for:
    • Experiment tracking: Log, display, organize, and compare ML experiments in a single place.
    • Model registry: Version, store, manage, and query trained models, and model building metadata.
    • Monitoring ML runs live: Record and monitor model training, evaluation, or production runs live
    For more information see <https://neptune.ai/>.
	"""
	
	homepage = "https://github.com/neptune-ai/neptune-r"
	cran = "neptune" 

	version("0.2.3", md5="cd77cac0b8507cdcbeed65fd7cb0a004")

	depends_on("r-reticulate@1.22:", type=("build", "run"))
	depends_on("r-this-path@0.4.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.7:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-plotly@4.9.4.1:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.5.3:", type=("build", "run"))
	depends_on("python@3.0.0:", type=("build", "link", "run"))
