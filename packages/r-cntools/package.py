# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCntools(RPackage):
	"""Convert segment data into a region by sample matrix to allow for other high level computational analyses.

	This package provides tools to convert the output of segmentation analysis using DNAcopy to a matrix structure with overlapping segments as rows and samples as columns so that other computational analyses can be applied to segmented data
	"""
	
	bioc = "CNTools"

	version("1.64.0", commit="c76377ab4cf46558d5bd1324520fc641b9b64f00")
	version("1.58.0", commit="fcce4a5a277bc399631d0957688e56e1186fbc16")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
