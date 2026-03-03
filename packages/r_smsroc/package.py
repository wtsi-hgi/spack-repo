# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmsroc(RPackage):
	"""Assessment of Diagnostic and Prognostic Markers

	Provides estimations of the Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) based on the two-stages mixed-subjects ROC curve estimator (Diaz-Coto et al. (2020) <doi:10.1515/ijb-2019-0097> and Diaz-Coto et al. (2020) <doi:10.1080/00949655.2020.1736071>).
	"""
	
	cran = "sMSROC" 

	version("0.1.2", md5="d196972faa0c7a5a932bd5eea864b6a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-plotroc", type=("build", "run"))
	depends_on("r-icenreg", type=("build", "run"))
	depends_on("r-thregi", type=("build", "run"))
