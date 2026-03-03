# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnifiedwmwqpcr(RPackage):
	"""Unified Wilcoxon-Mann Whitney Test for testing differential expression in qPCR data

	This packages implements the unified Wilcoxon-Mann-Whitney Test for qPCR data. This modified test allows for testing differential expression in qPCR data.
	"""
	
	bioc = "unifiedWMWqPCR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/unifiedWMWqPCR_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/unifiedWMWqPCR/unifiedWMWqPCR_1.38.0.tar.gz"]

	version("1.38.0", md5="d9a09d196f72dc2246328247851dd24a")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-htqpcr", type=("build", "run"))
