# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcpmor(RPackage):
	"""Two Cut-Points with Maximum Odds Ratio

	Enables the computation of the 'two cut-points with maximum odds ratio (OR)
    value method' for data analysis, particularly suited for binary classification
    tasks. Users can identify optimal cut-points in a continuous variable by
    maximizing the odds ratio while maintaining an equal risk level, useful for
    tasks such as medical diagnostics, risk assessment, or predictive modeling.
	"""
	
	cran = "TCPMOR" 

	version("1.0", md5="1104095094cb0fbe55f799a4addbeedb")

	depends_on("r-semipar", type=("build", "run"))
