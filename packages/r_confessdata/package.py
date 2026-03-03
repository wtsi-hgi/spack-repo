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

	version("1.30.0", md5="07df3f8f783b3e734c4032b3f6ed61bd")

	depends_on("r@3.3:", type=("build", "run"))

