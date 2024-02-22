# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnageedata(RPackage):
	"""SNAGEE data

	SNAGEE data - gene list and correlation matrix
	"""
	
	homepage = "http://fleming.ulb.ac.be/SNAGEE"
	bioc = "SNAGEEdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/SNAGEEdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/SNAGEEdata/SNAGEEdata_1.38.0.tar.gz"]

	version("1.38.0", md5="bfd0a2689cb9ac612cb2f8995c3a03d5")

	depends_on("r@2.6:", type=("build", "run"))

	# experiment