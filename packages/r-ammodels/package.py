# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmmodels(RPackage):
	"""Adaptive Management Model Manager

	Helps enable adaptive management by codifying knowledge in the
    form of models generated from numerous analyses and data sets. Facilitates
    this process by storing all models and data sets in a single object that can
    be updated and saved, thus tracking changes in knowledge through time. A shiny
    application called AM Model Manager (modelMgr()) enables the use of these
    functions via a GUI.
	"""
	
	cran = "AMModels" 

	version("0.1.4", md5="fa9634e2c63a2618ca0f5b7b35b381e9")

	depends_on("r-unmarked", type=("build", "run"))
