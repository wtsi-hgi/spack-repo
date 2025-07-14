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

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="edd56d5071863d4e4a97db601e2174cff243fb2104b13ad9eec6603baabd726c")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-htqpcr", type=("build", "run"))
