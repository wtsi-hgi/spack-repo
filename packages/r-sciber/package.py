# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSciber(RPackage):
	"""Single-Cell Integrator and Batch Effect Remover

	Remove batch effects by projecting query batches into the reference batch space.
	"""
	
	homepage = "https://github.com/RavenGan/SCIBER"
	cran = "SCIBER" 

	version("0.2.2", md5="66e4fd27209269a6508b47f91a3ee29a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
