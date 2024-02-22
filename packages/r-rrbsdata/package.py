# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrbsdata(RPackage):
	"""An RRBS data set with 12 samples and 10,000 simulated DMRs

	RRBS data set comprising 12 samples with simulated differentially methylated regions (DMRs).
	"""
	
	bioc = "RRBSdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/RRBSdata_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/RRBSdata/RRBSdata_1.22.0.tar.gz"]

	version("1.22.0", md5="04bcf0f0348dc54984ca9506773820ec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biseq@1.9.2:", type=("build", "run"))

	# experiment