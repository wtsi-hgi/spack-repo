# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsseqdata(RPackage):
	"""Example whole genome bisulfite data for the bsseq package

	Example whole genome bisulfite data for the bsseq package
	"""
	
	bioc = "bsseqData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/bsseqData_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/bsseqData/bsseqData_0.40.0.tar.gz"]

    version("0.46.0", tag="RELEASE_3_21")
	version("0.40.0", sha256="d2506f1e11b5cb48e7559f209fef682d6055f8ebcfdd8ec97444e965a8d9de95")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsseq@1.16:", type=("build", "run"))

