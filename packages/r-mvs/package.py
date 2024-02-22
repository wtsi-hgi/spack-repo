# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvs(RPackage):
	"""Methods for High-Dimensional Multi-View Learning

	Methods for high-dimensional multi-view learning based on the multi-view stacking (MVS) framework.
    For technical details on the MVS and stacked penalized logistic regression (StaPLR) methods see Van Loon, Fokkema, Szabo, & De Rooij (2020) <doi:10.1016/j.inffus.2020.03.007> and Van Loon et al. (2022) <doi:10.3389/fnins.2022.830630>. 
	"""
	
	cran = "mvs" 

	version("1.0.2", md5="9329b1f6e029cb03cd35a19a9b4dd388")

	depends_on("r-glmnet@1.9.8:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
