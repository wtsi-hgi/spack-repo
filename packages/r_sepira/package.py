# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSepira(RPackage):
	"""Systems EPigenomics Inference of Regulatory Activity

	SEPIRA (Systems EPigenomics Inference of Regulatory Activity) is an algorithm that infers sample-specific transcription factor activity from the genome-wide expression or DNA methylation profile of the sample.
	"""
	
	bioc = "SEPIRA" 

	version("1.22.0", commit="238b1ee722f8356a8bf6b926b87ad9458c00926b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-limma@3.32.5:", type=("build", "run"))
	depends_on("r-corpcor@1.6.9:", type=("build", "run"))
