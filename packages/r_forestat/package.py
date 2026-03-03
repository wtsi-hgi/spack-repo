# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestat(RPackage):
	"""Forest Carbon Sequestration and Potential Productivity
Calculation

	Include assessing site classes based on the stand height growth and establishing a nonlinear mixed-effect biomass model under different site classes based on the whole stand model to achieve more accurate estimation of carbon sequestration. In particular, a carbon sequestration potential productivity calculation method based on the potential mean annual increment is proposed. This package is applicable to both natural forests and plantations. It can quantitatively assess stand’s potential productivity, realized productivity, and possible improvement under certain site, and can be used in many aspects such as site quality assessment, tree species suitability evaluation, and forest degradation evaluation. Reference: Lei X, Fu L, Li H, et al (2018) <doi:10.11707/j.1001-7488.20181213>. Fu L, Sharma R P, Zhu G, et al (2017) <doi:10.3390/f8040119>.
	"""
	
	homepage = "https://github.com/caf-ifrit/forestat"
	cran = "forestat" 

	version("1.1.0", md5="370941028342955651c4bd3e52c05d8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
