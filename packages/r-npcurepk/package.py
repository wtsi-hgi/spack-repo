# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpcurepk(RPackage):
	"""Mixture Cure Model Estimation with Cure Status Partially Known

	Performs nonparametric estimation in mixture cure models when the cure status is partially known. For details, see Safari et al (2021) <doi:10.1002/bimj.202100156>, Safari et al (2022) <doi:10.1177/09622802221115880> and Safari et al (2023) <doi:10.1007/s10985-023-09591-x>.
	"""
	
	cran = "npcurePK" 

	version("1.0-2", md5="e5d4a684302347dc18b6f9b0a73e3f04")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-npcure", type=("build", "run"))
