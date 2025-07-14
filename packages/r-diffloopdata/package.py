# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffloopdata(RPackage):
	"""Example ChIA-PET Datasets for the diffloop Package

	ChIA-PET example datasets and additional data for use with the diffloop package.
	"""
	
	bioc = "diffloopdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/diffloopdata_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/diffloopdata/diffloopdata_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="0a2b0375b84d9d4a4a5ae0637f9298a9bfb329f916de25da3c7ecd2e2fb70fb8")


