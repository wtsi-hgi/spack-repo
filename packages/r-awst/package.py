# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwst(RPackage):
	"""Asymmetric Within-Sample Transformation

	We propose an Asymmetric Within-Sample Transformation (AWST) to regularize RNA-seq read counts and reduce the effect of noise on the classification of samples. AWST comprises two main steps: standardization and smoothing. These steps transform gene expression data to reduce the noise of the lowly expressed features, which suffer from background effects and low signal-to-noise ratio, and the influence of the highly expressed features, which may be the result of amplification bias and other experimental artifacts.
	"""
	
	homepage = "https://github.com/drisso/awst"
	bioc = "awst" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/awst_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/awst/awst_1.10.0.tar.gz"]

	version("1.10.0", md5="a7ca0636a8f728b63d6cf56729b856eb")

	depends_on("r-summarizedexperiment", type=("build", "run"))
