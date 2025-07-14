# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfessdata(RPackage):
	"""Example dataset for CONFESS package

	Example text-converted C01 image files for use in the CONFESS Bioconductor package.
	"""
	
	bioc = "CONFESSdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CONFESSdata_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CONFESSdata/CONFESSdata_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="c427976846da45a0673790971a8ff75245982f063446c929501a1bf0735e5abe")

	depends_on("r@3.3:", type=("build", "run"))

