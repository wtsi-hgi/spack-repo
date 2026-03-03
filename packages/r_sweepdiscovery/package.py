# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSweepdiscovery(RPackage):
	"""Selective Sweep Discovery Tool

	Selective sweep is a biological phenomenon in which genetic variation between neighboring beneficial mutant alleles is swept away due to the effect of genetic hitchhiking. Detection of selective sweep is not well acquainted as well as it is a laborious job. This package is a user friendly approach for detecting selective sweep in genomic regions. It uses a Random Forest based machine learning approach to predict selective sweep from VCF files as an input. Input of this function, train data and new data, can be computed using the project <https://github.com/AbhikSarkar1999/SweepDiscovery> in 'GitHub'. This package has been developed by using the concept of  Pavlidis and Alachiotis (2017) <doi:10.1186/s40709-017-0064-0>.
	"""
	
	cran = "SweepDiscovery" 

	version("0.1.1", md5="e558ca8baf120ba06006747eb2728ee3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
