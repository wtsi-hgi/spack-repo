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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/quantsmooth_1.68.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/quantsmooth/quantsmooth_1.68.0.tar.gz"]

	version("1.68.0", md5="cb47e0040fd219ad15aebf094dd379cd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
