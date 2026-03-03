# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNovelforestsg(RPackage):
	"""Dataset from the Novel Forests of Singapore

	
    The raw dataset and model used in Lai et al. (2021) 
    Decoupled responses of native and exotic tree diversities to 
    distance from old-growth forest and soil phosphorous in 
    novel secondary forests. Applied Vegetation Science, 24, e12548.
	"""
	
	homepage = "https://hrlai.github.io/novelforestSG/"
	cran = "novelforestSG" 

	version("2.1.0", md5="9c2a4bfa13132840a4784ecf97655639")

	depends_on("r@3.5:", type=("build", "run"))
