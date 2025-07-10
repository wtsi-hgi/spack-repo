# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabocoreutils(RPackage):
	"""Core Utils for Metabolomics Data

	MetaboCoreUtils defines metabolomics-related core functionality provided as low-level functions to allow a data structure-independent usage across various R packages. This includes functions to calculate between ion (adduct) and compound mass-to-charge ratios and masses or functions to work with chemical formulas. The package provides also a set of adduct definitions and information on some commercially available internal standard mixes commonly used in MS experiments.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MetaboCoreUtils"
	bioc = "MetaboCoreUtils" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MetaboCoreUtils_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MetaboCoreUtils/MetaboCoreUtils_1.10.0.tar.gz"]

	version("1.10.0", sha256="b491e54bac78a8edbb84158748e503d8847d6828bac930c4d511558a7923422f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
