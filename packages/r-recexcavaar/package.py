# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecexcavaar(RPackage):
	"""3D Reconstruction of Archaeological Excavations

	A toolset for 3D reconstruction and analysis of excavations. It provides methods to reconstruct natural and artificial surfaces based on field measurements. This allows to spatially contextualize documented subunits and features. Intended to be part of a 3D visualization workflow.
	"""
	
	homepage = "https://github.com/ISAAKiel/recexcavAAR"
	cran = "recexcavAAR" 

	version("0.3.0", md5="fc058e491909efceab77824316217bb0")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-kriging@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
