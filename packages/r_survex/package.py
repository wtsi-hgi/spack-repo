# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvex(RPackage):
	"""Explainable Machine Learning in Survival Analysis

	Survival analysis models are commonly used in medicine and other areas. Many of them
    are too complex to be interpreted by human. Exploration and explanation is needed, but
    standard methods do not give a broad enough picture. 'survex' provides easy-to-apply
    methods for explaining survival models, both complex black-boxes and simpler statistical models.
    They include methods specific to survival analysis such as SurvSHAP(t) introduced in Krzyzinski et al., (2023)
    <doi:10.1016/j.knosys.2022.110234>, SurvLIME described in Kovalev et al., (2020) <doi:10.1016/j.knosys.2020.106164> as well as
    extensions of existing ones described in Biecek et al., (2021) <doi:10.1201/9780429027192>.
	"""
	
	homepage = "https://modeloriented.github.io/survex/"
	cran = "survex" 

	version("1.2.0", md5="b1dff27eaff789636dda7efb6a7c64a5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dalex@2.2.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-kernelshap", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
