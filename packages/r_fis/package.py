# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFis(RPackage):
	"""Human Functional Interactions (FIs) for splineTimeR package

	Data set containing two complete lists of identified functional interaction partners in Human. Data are derived from Reactome and BioGRID databases.
	"""
	
	bioc = "FIs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FIs_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FIs/FIs_1.30.0.tar.gz"]

	version("1.30.0", md5="ef807b75136742a1dcb5ea70993d5c38")

	depends_on("r@3.3:", type=("build", "run"))

