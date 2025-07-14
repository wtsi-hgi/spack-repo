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

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="64adfbe1a4b1cea71071ed4573126b7b2d25f4d162bcb08e0239e464c505dc5e")

	depends_on("r@3.3:", type=("build", "run"))

