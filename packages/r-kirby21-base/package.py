# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKirby21Base(RPackage):
	"""Example Data from the Multi-Modal MRI 'Reproducibility' Resource

	Multi-modal magnetic resonance imaging ('MRI')
    data from the 'Kirby21' 'reproducibility' study
    <https://www.nitrc.org/projects/multimodal/>, including functional
    and structural imaging.
	"""
	
	homepage = "https://www.nitrc.org/projects/multimodal/"
	cran = "kirby21.base" 

	version("1.7.3", md5="7028abe16f76950e5ff4c8f6a9e10aff")

	depends_on("r-git2r", type=("build", "run"))
