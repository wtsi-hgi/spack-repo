# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioInfer(RPackage):
	"""Predict Environmental Conditions from Biological Observations

	Imports benthic count data, reformats this data, and
        computes environmental inferences from this data.
	"""
	
	cran = "bio.infer" 

	version("1.3-6", md5="44342ee888bcc59ddb14260102d1c0b3")

	depends_on("r@2.10:", type=("build", "run"))
