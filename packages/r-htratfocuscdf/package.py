# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtratfocuscdf(RPackage):
	"""htratfocuscdf

	A package containing an environment representing the HT_Rat-Focus.cdf file.
	"""
	
	bioc = "htratfocuscdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/htratfocuscdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/htratfocuscdf/htratfocuscdf_2.18.0.tar.gz"]

	version("2.18.0", md5="04b4952f7d8b607a7eb0f779c08c57dc")

	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation