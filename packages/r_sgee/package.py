# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgee(RPackage):
	"""Stagewise Generalized Estimating Equations

	Stagewise techniques implemented with Generalized Estimating Equations to handle individual, group, bi-level, and interaction selection. Stagewise approaches start with an empty model and slowly build the model over several iterations, which yields a 'path' of candidate models from which model selection can be performed. This 'slow brewing' approach gives stagewise techniques a unique flexibility that allows simple incorporation of Generalized Estimating Equations; see Vaughan, G., Aseltine, R., Chen, K., Yan, J., (2017) <doi:10.1111/biom.12669> for details.
	"""
	
	cran = "sgee" 

	version("0.6-0", md5="d04f74a16af79a8a28dc13970676130c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
