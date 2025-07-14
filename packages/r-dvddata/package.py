# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDvddata(RPackage):
	"""Drug versus Disease Data

	Data package which provides default drug and disease expression profiles for the DvD package.
	"""
	
	bioc = "DvDdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DvDdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DvDdata/DvDdata_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="c36cca1c305bc0e67da88ca0a239b6c34e6993c6a93fb70096ba7c4506146598")

	depends_on("r@2.10:", type=("build", "run"))

