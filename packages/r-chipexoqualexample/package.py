# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipexoqualexample(RPackage):
	"""Example data for the ChIPexoQual package, which implements a quality control pipeline for ChIP-exo data

	Data for the ChIPexoQual package, consisting of (3) chromosome 1 aligned reads from a ChIP-exo experiment for FoxA1 in mouse liver cell lines aligned to the mm9 genome.
	"""
	
	homepage = "http://www.github.com/keleslab/ChIPexoQualExample"
	bioc = "ChIPexoQualExample" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ChIPexoQualExample_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ChIPexoQualExample/ChIPexoQualExample_1.26.0.tar.gz"]

	version("1.26.0", md5="5ebb67a1848aa0e69557e795d236e24b")

	depends_on("r@3.3:", type=("build", "run"))

	# experiment