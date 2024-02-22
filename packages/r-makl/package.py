# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakl(RPackage):
	"""Multiple Approximate Kernel Learning (MAKL)

	R package associated with the Multiple Approximate Kernel Learning (MAKL) algorithm proposed in <doi:10.1093/bioinformatics/btac241>. The algorithm fits multiple approximate kernel learning (MAKL) models that are fast, scalable and interpretable. 
	"""
	
	cran = "MAKL" 

	version("1.0.1", md5="c30d809f64ddca1226325092e0854b15")

	depends_on("r-auc", type=("build", "run"))
	depends_on("r-grplasso", type=("build", "run"))
