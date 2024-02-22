# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RText2sdgdata(RPackage):
	"""Contains the Trained 'text2sdg' Ensemble Model Data

	This is a companion package for the 'text2sdg' package. It contains the trained ensemble models needed by the 'detect_sdg' function from the 'text2sdg' package. See Wulff, Meier and Mata (2023) <arXiv:2301.11353> and Meier, Wulff and Mata (2021) <arXiv:2110.05856> for reference.
	"""
	
	homepage = "https://github.com/psychobas/text2sdgData"
	cran = "text2sdgData" 

	version("0.1.1", md5="d6dcfdd717078c5fed04a4f47641026f")

	depends_on("r@2.10:", type=("build", "run"))
