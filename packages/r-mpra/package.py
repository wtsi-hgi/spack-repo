# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpra(RPackage):
	"""Analyze massively parallel reporter assays

	Tools for data management, count preprocessing, and differential analysis in massively parallel report assays (MPRA).
	"""
	
	homepage = "https://github.com/hansenlab/mpra"
	bioc = "mpra" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mpra_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mpra/mpra_1.24.0.tar.gz"]

    version("1.30.1", tag="RELEASE_3_21")
	version("1.24.0", sha256="78cdb3a36b182af6ac187fb65e88b0d0321b3b33da19b3463a40723da9a24d7d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
