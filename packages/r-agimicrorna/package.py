# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgimicrorna(RPackage):
	"""Processing and Differential Expression Analysis of Agilent microRNA
	   chips.

	Processing and Analysis of Agilent microRNA data."""

	bioc = "AgiMicroRna"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AgiMicroRna_2.52.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AgiMicroRna/AgiMicroRna_2.52.0.tar.gz"]

	version("2.52.0", md5="1c1046ab29a7766af0c602c974b4ec21")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-affy@1.22:", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-affycoretools", type=("build", "run"))
