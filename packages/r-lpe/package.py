# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpe(RPackage):
	"""Methods for analyzing microarray data using Local Pooled Error (LPE) method

	This LPE library is used to do significance analysis of microarray data with small number of replicates. It uses resampling based FDR adjustment, and gives less conservative results than traditional 'BH' or 'BY' procedures. Data accepted is raw data in txt format from MAS4, MAS5 or dChip. Data can also be supplied after normalization. LPE library is primarily used for analyzing data between two conditions. To use it for paired data, see LPEP library. For using LPE in multiple conditions, use HEM library.
	"""
	
	homepage = "http://www.r-project.org"
	bioc = "LPE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LPE_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LPE/LPE_1.76.0.tar.gz"]

    version("1.82.0", tag="RELEASE_3_21")
	version("1.76.0", sha256="09b7b5f563be2cd30d15f8e40a8d6660401609bd6e09bdc04060fed1abf21a46")

	depends_on("r@2.10:", type=("build", "run"))
