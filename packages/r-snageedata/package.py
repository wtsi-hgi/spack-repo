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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SNAGEEdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SNAGEEdata/SNAGEEdata_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="76ded9fe3edf46e0f928499e701a7a11581a97dcf39479e5f7794aaa3b718b9f")

	depends_on("r@2.6:", type=("build", "run"))

