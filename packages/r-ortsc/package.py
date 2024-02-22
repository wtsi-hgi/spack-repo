# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrtsc(RPackage):
	"""Connects to Google Cloud API for Label Detection

	Connects to Google cloud vision <https://cloud.google.com/vision> to perform label detection and repurpose this feature for image classification.
	"""
	
	homepage = "https://github.com/MohmedSoudy/ORTSC"
	cran = "ORTSC" 

	version("1.0.0", md5="dfdf68de111c4a5c9745fe1f740194b2")

	depends_on("r-googleauthr", type=("build", "run"))
	depends_on("r-googlecloudvisionr", type=("build", "run"))
