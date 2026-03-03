# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdpm(RPackage):
	"""Data Sets for Discrete Probability Models

	A wide collection of univariate discrete data sets from various applied domains related to distribution theory. The functions allow quick, easy, and efficient access to 100 univariate discrete data sets. The data are related to different applied domains, including medical, reliability analysis, engineering, manufacturing, occupational safety, geological sciences, terrorism, psychology, agriculture, environmental sciences, road traffic accidents, demography, actuarial science, law, and justice. The documentation, along with associated references for further details and uses, is presented.     
	"""
	
	cran = "DDPM" 

	version("0.1.0", md5="04230f1edcdd11699078d7c4627870a5")

	depends_on("r@4:", type=("build", "run"))
