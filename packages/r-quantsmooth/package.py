# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantsmooth(RPackage):
	"""Quantile smoothing and genomic visualization of array data

	Implements quantile smoothing as introduced in: Quantile smoothing of array CGH data; Eilers PH, de Menezes RX; Bioinformatics. 2005 Apr 1;21(7):1146-53.
	"""
	
	bioc = "quantsmooth" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/quantsmooth_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/quantsmooth/quantsmooth_1.68.0.tar.gz"]

	version("1.74.0", tag="RELEASE_3_21")
	version("1.68.0", sha256="0a810f64fbaf3c07447602ec3d7dcff973d306634446e34a308d8ed921b71614")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
