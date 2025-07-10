# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChickencdf(RPackage):
	"""chickencdf

	A package containing an environment representing the Chicken.cdf file.
	"""
	
	bioc = "chickencdf" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/chickencdf_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/chickencdf/chickencdf_2.18.0.tar.gz"]

	version("2.18.0", sha256="e1d3be18cefe3b5884a6628b9c81adc2535cdcd6c1c25c96b047f6a44b8d1026")

	depends_on("r-annotationdbi", type=("build", "run"))

